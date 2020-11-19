import papermill as pm
import warnings
import logging

logging.getLogger('papermill')
logging.basicConfig(level='INFO', format="%(message)s")
warnings.filterwarnings('ignore')
    
pm.execute_notebook(
    input_path="classification-19-1.ipynb",
    output_path="output_classification-19-1.ipynb",
    parameters=None,
    engine_name=None,
    request_save_on_cell_execute=True,
    prepare_only=False,
    kernel_name=None,
    progress_bar=True,
    log_output=True,
    stdout_file=None,
    stderr_file=None,
    start_timeout=60,
    report_mode=False,
    cwd=None,
)
