import multiprocessing

"""
    This decorator works on linux, but not on Windows.
    Windows identifies that func called by Process()
    is not the same as the function on __main__
    (because it is wrapped by the decorator).

"""


def run_with_timeout(timeout=10, verbose=False):
    """
        Run `func` as a separate process.
        Wait for `timeout` seconds or until process finishes.

    """

    def timeout_func(func):

        def wrapper_func(*args, **kwargs):
            if verbose:
                print("*" * 30)
                print("Verbose is active")
                print(f"timeout={timeout} s")
                print(f"args: {args} \nkwargs: {kwargs}")
                print("*" * 30)
            p = multiprocessing.Process(target=func, args=args, kwargs=kwargs)
            p.start()
            # Wait for 10 seconds or until process finishes
            p.join(timeout)
            # If thread is still active
            if p.is_alive():
                # Terminate - may not work if process is stuck for good
                p.terminate()
                # OR Kill - will work for sure, no chance for process to finish nicely however
                # p.kill()
                p.join()
                return False
            return True

        return wrapper_func

    return timeout_func


if __name__ == "__main__":
    #
    # sample function to test
    #
    @run_with_timeout(timeout=5)
    def func(arg="Test"):
        print("This is a", arg)
    func(arg="My test")

    @run_with_timeout(timeout=0.5, verbose=True)
    def func2(arg="Test", timeout=2):
        print("->>><<<-")
        import time
        time.sleep(timeout)
        print("This is a", arg)
    func2(arg="Show this text", timeout=0)
    func2(arg="Don't show this text")
    """
        should return:

        This is a My test
        ******************************
        Verbose is active
        timeout=0.5 s
        args: ()
        kwargs: {'arg': 'Show this text', 'timeout': 0}
        ******************************
        ->>><<<-
        This is a Show this text
        ******************************
        Verbose is active
        timeout=0.5 s
        args: ()
        kwargs: {'arg': "Don't show this text"}
        ******************************
    """
