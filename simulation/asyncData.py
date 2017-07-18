import asyncio
import random

class AsyncData():
    def __init__(self,fn):
        self.task=asyncio.Task(self.periodic(fn))

    @asyncio.coroutine
    def periodic(self,fn):
        while True:
            newData=self.genData()
            print(newData)
            fn(newData)
            yield from asyncio.sleep(random.randint(1,3))

    def genData(self):
        pos='<pos>'+self.genPos()+'</pos>'
        msg='<msg>saya disini loh</msg>'
        newData='<body>'+pos+'\n'+msg+'</body>'
        return newData

    def genPos(self):
        value=['gbsvh','gbsvj','gbsvn','gbsuu','gbsuv',
                'gbsuy','gbsus','gbsut','gbsuw']
        return random.choice(value)
                                
    
    def stop(self):
        self.task.cancel()
        
    def start(self,elapse):
        loop=asyncio.get_event_loop()
        loop.call_later(elapse,self.stop)
        try:
            loop.run_until_complete(self.task)
        except asyncio.CancelledError:
            pass
