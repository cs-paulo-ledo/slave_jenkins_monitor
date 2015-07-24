# slave_jenkins_monitor
Monitora os slaves Jenkins atraves da api fornecida pelo o Jenkins Master
. Caso o slave esteja fora do ar o script inicia-o novamente


---------------------
ToDo

- instalação das dependendcias
- Logs
- Multiplos slaves na mesma maquina


------------------------

Exemplo de arquivo de configuracao:

---

CI_API_URL: http://10.3.13.9:8080/computer/api/json
SCRIPT_DIRECTORY: /home/slave_jenkins/scripts/
PROJECT_NAME: ci__project
SLAVE_USER: slave_jenkins
SLAVE_NAME: slave_jenkins__android
SLAVE_URL: http://10.3.13.9:8080/computer/TITANS-SLAVE/slave-agent.jnlp
SLAVES_REQUIRED:
    - slave_name: slave_jenkins_android
      slave_url: SLAVE_URL: http://10.3.13.9:8080/computer/TITANS-SLAVE/slave-agent.jnlp
SLAVES_REQUIRED:
      slave_user: slave_jenkins

Após definir no arquivo de configuracao as informacoes, podemos configurar
uma task no cron do user que sobe o slave, por exemplo:

*/5 * * * * $(cd diretorio_script ; python slave_jenkins_monitor)
