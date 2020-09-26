class Form:


    def __init__(self, action, method, parameter):
        self.__action = action;
        self.__method = method;
        self.__parameter = parameter;

    @property
    def action(self):
        return self.__action
    @action.setter    
    def action(self, action):
        self.__action = action

    @property
    def method(self):
        return self.__method
    @method.setter    
    def method(self, method):
        self.__method = method

    @property
    def parameter(self):
        return self.__parameter
    @parameter.setter    
    def parameter(self, parameter):
        self.__parameter = parameter
