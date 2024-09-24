import subprocess

def run_script(script_name):
    subprocess.run(['python', script_name])

if __name__ == "__main__":
    run_script('datas/database.py')
    run_script('datas/import_data.py')
    run_script('vues.py')
    run_script('procedure.py')
    run_script('triggers.py')
    run_script('question5.py')
    run_script('app.py')

    
