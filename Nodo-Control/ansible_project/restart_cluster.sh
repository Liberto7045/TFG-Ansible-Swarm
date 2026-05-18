#!/bin/bash
echo "Reiniciando Docker en todos los nodos..."
ansible swarm_nodes -i ~/ansible_project/hosts -m shell -a "sudo systemctl restart docker" -b
sleep 15
echo "Redesplegando stack..."
ssh swarmmanager@192.168.56.11 "sudo docker stack deploy -c /home/swarmmanager/stack.yml mi_proyecto"
echo "Listo."

