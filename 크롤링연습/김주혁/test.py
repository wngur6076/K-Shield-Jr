class Form:

    def __init__(self, action, method, parameter):
        self.__action = action
        self.__method = method
        self.__parameter = parameter
        self.__query = 'default'

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
    def query(self):
        return self.__query
    @query.setter    
    def query(self, query):
        self.__query = query
    
    def get_parameter(self):
        if self.__method == 'get':       
            url = str()
            for key, val in self.__parameter.items():
                url = url + '&' + key + '=' + (val == None and self.__query or val)
            
            return url.replace('&', '?', 1)
        
        if self.__method == 'post':
            info = list()
            for key, val in self.__parameter.items():
                info.append([key, val == None and self.__query or val])
            return dict(info)
