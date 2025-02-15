import ast


class Storage:

    def string_to_list(self, input_string):
        try:
            result = ast.literal_eval(input_string)
            if isinstance(result, list):
                return result
            else:
                raise ValueError("A string fornecida não é uma lista válida.")
        except Exception as e:
            raise ValueError(f"Erro ao converter a string: {e}")
