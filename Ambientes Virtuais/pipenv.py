## Pipenv é uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências com a criação de ambiente virtual para seus projetos e adiciona/remove
## pacotes automaticamente do arquivo Pipfile conforme você instala e desinstala pacotes.

pip install pipenv
# 
pipenv install django
## Para visualizar conteúdo do arquivo use os comandos:
type Pipfile
get-content Pipfile
# Ambos irão fornecer o mesmo resultado abaixo:

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"

[dev-packages]

[requires]
python_version = "3.12"

# USANDO O GET-CONTENT PARA VISUALIZAR O ARQUIVO 'Pipfile.lock' :
get-content Pipfile.lock
{
    "_meta": {
        "hash": {
            "sha256": "0b5823de65ff0f5100b8f0fd7642f5000e8f2788c925cc51afe587d419e35515"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.12"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "asgiref": {
            "hashes": [
                "sha256:3e1e3ecc849832fe52ccf2cb6686b7a55f82bb1d6aee72a58826471390335e47",
                "sha256:c343bd80a0bec947a9860adb4c432ffa7db769836c64238fc34bdc3fec84d590"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==3.8.1"
        },
        "django": {
            "hashes": [
                "sha256:8363ac062bb4ef7c3f12d078f6fa5d154031d129a15170a1066412af49d30905",
                "sha256:ff1b61005004e476e0aeea47c7f79b85864c70124030e95146315396f1e7951f"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.10'",
            "version": "==5.0.6"
        },
        "sqlparse": {
            "hashes": [
                "sha256:714d0a4932c059d16189f58ef5411ec2287a4360f17cdd0edd2d09d4c5087c93",
                "sha256:c204494cd97479d0e39f28c93d46c0b2d5959c7b9ab904762ea6c7af211c8663"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.5.0"
        },
        "tzdata": {
            "hashes": [
                "sha256:2674120f8d891909751c38abcdfd386ac0a5a1127954fbc332af6b5ceae07efd",
                "sha256:9068bc196136463f5245e51efda838afa15aaeca9903f49050dfa2679db4d252"
            ],
            "markers": "sys_platform == 'win32'",
            "version": "==2024.1"
        }
    },
    "develop": {}
}
