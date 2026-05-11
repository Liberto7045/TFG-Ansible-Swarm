k#!/bin/bash
echo "Reiniciando Docker en todos los nodos..."
ansible swarm_nodes -i ~/ansible_project/hosts -m shell -a "sudo systemctl >
sleep 25
echo "Redesplegando stack..."
ssh swarmmanager@192.168.56.11 "sudo docker stack rm mi_proyecto && sleep 1>
echo "Listo."
