from cx_Freeze import setup, Executable

settings = Executable( 
    script='app.py',
    icon='dolar.ico'
)

setup( 
    name='Preco do Dolar',
    version='1.0',
    description='Monitore o preco do dolar no periodo que desejar.',
    author='Jonatas Lopes de Sousa',
    options={'build_exe':{
        'include_msvcr': True
    }}, 
    executables=[settings]),
    