import logging
import sys
import time
import traceback
sys.path.append('./src')

from app.database.classromStorage import classrom_storage
from app.database.classDemandStorage import class_demand_storage
from fastapi import APIRouter, status, Response
from typing import List
from model.classDemand import ClassDemand
from scripts.classCSP import classCSP
from scripts.generateClasses import GenerateClasses
from scripts.backTracking import BackTracking
from scripts.constraint import constraint as Constraint
from scripts.interface import Interface



router = APIRouter()

@router.post("/run/start", status_code=status.HTTP_201_CREATED, tags=["Run"])
def start_classroms(demand: List[ClassDemand], response: Response):
    try:
        for classrom in demand:
            class_demand_storage.add_class_demand(classrom.recover_discipline())
        response.status_code = status.HTTP_201_CREATED
        logging.info("Started new classroms")
        class_demand_storage.save_class_demands('./src/data/classroms-demand.txt')

        locals = classrom_storage.list_classroms()
        print(f'Quantidade de locais {len(locals)}')
        class_demand = class_demand_storage.return_class_demands()
        cources = GenerateClasses(class_demand)
        days = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
        horarios = [
        '10:00-11:50', '08:00-09:50', '16:00-17:50',
        '14:00-15:50'
        ]

        tempo_inicial = time.time()
        turmas = cources.get_classroom()
        print(f'Quantidade de turmas {len(turmas)}')
        restrincao = Constraint()
        csp = classCSP(
            locals = locals,
            days = days,
            times = horarios,
            cources = turmas,
            constraint = restrincao
        )
        csp.init_variables()
        csp.sort_variables()
        # print(csp)
        back_tracking_search = BackTracking(csp)
        assigment_list = []

        try:
            assigment = back_tracking_search.search(len(turmas), assigment_list)
        except Exception as e:
            print(f"⚠️ Erro detectado em search: {e}")
            traceback.print_exc()

        tempo_final = time.time()
        duracao = tempo_final - tempo_inicial
        if assigment:  # Se search retornou algo diferente de False
            ui = Interface(assigment)
            ui.draw()
        else:
            print("❌ Nenhuma solução encontrada!")
        
        # Exibir os resultados
        print(f"Tempo inicial: {tempo_inicial:.6f} segundos")
        print(f"Tempo final: {tempo_final:.6f} segundos")
        print(f"Duração da execução: {duracao:.6f} segundos")
        
        return {
            "message": f"Classroms started successfully",
            "duration": f"{duracao:.6f} seconds",
            "classroms": len(turmas),
            "timetable": assigment
            }
    except Exception as e:
        logging.error(f"Error starting a new classrom: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Internal Server Error"}
