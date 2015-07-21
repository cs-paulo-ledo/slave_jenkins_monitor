# slave_jenkins_monitor
Monitora os slaves Jenkins, caso esteja fora do ar, sobe


---------------------
ToDo

- instalação das dependendcias
- Logs


------------------------

exemplo de arquivo de configuracao:

---

CI_API_URL: http://10.3.13.9:8080/computer/api/json
CWD: /home/devops/scripts
PROJECT_NAME: cl-idios
USER: jenkins 
CI_GROUP_ID: 1003
SLAVE_NAME: TITANS-SLAVE
URL: http://10.3.13.9:8080/computer/TITANS-SLAVE/slave-agent.jnlp
SLAVES_REQUIRED:
    - TITANS-SLAVE
    
    
no Jenkins master criei um job assim:

#!/bin/bash
cd /home/jenkins/devops/projetos/scripts/slave_jenkins_monitor/
sudo nohup python slave_jenkins_monitor.py
