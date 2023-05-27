import pytest
from workers.register import WorkerRegister



def test_worker_register():
    register = WorkerRegister()

    @register(1)
    class Worker01:
        pass

    @register(2)
    class Worker02:
        pass

    @register(3)
    class Worker03:
        pass

    assert len(register) == 3
    assert register.get_worker(1) is Worker01
    assert register.get_worker(2) is Worker02
    assert register.get_worker(3) is Worker03

    with pytest.raises(Exception, match='Worker 4 not found'):
        register.get_worker(4)


