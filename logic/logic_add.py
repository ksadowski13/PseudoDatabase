from logic.logic_default import DefaultLogic

class AddLogic(DefaultLogic):
    def __init__(self, document_name, columns, values):
        super(AddLogic, self).__init__(document_name, columns, values)

    def file_operation(self):
        self.file_handler.add_record(self.document_name, self.values)