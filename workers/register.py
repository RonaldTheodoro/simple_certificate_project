class WorkerRegister:
    __workers = {}

    def __call__(self, worker_id):
        def wrapper(worker_cls):
            self.__workers[worker_id] = worker_cls
            return worker_cls

        return wrapper

    def __len__(self):
        return len(self.__workers)

    def get_worker(self, worker_id):
        try:
            return self.__workers[worker_id]
        except KeyError as err:
            raise Exception(f"Worker {worker_id} not found") from err


register = WorkerRegister()
