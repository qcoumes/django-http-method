from django.http import HttpResponseNotAllowed


class HttpMethodMixin:
    allowed = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'TRACE']
    
    def dispatch(self, *args, **kwargs):
        data = self.request.POST if self.request.method == "POST" else self.request.GET
        method = data.get('_method')
        
        if method:
            if method not in self.allowed:
                return HttpResponseNotAllowed(self.allowed, "Method Not Allowed (" + method + ")")
            
            self.request.method = method
            self.request.META['REQUEST_METHOD'] = method
            setattr(self.request, method, data)
        
        return super(HttpMethodMixin, self).dispatch(*args, **kwargs)
