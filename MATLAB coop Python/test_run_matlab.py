import matlab.engine
eng = matlab.engine.start_matlab()
eng.MatLab_run_python(nargout=0)
