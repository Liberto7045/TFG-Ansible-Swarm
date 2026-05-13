# TFG — Automatización del Despliegue de un Clúster Docker Swarm con Ansible

**CFGS Administración de Sistemas Informáticos en Red (ASIR) · UAX FP · Curso 2025-2026**  
Alumno: Liberto Rodríguez Jullion · Tutor: Francisco Javier Segovia Bernardos

---

## Descripción

Este proyecto automatiza el despliegue de un clúster Docker Swarm en alta disponibilidad sobre cuatro máquinas virtuales Ubuntu 24.04, gestionado íntegramente mediante Ansible desde un nodo de control dedicado.

Con un único comando se despliega toda la infraestructura:

```bash
ansible-playbook -i ~/ansible_project/hosts ~/ansible_project/deploy_swarm.yml
```

## Arquitectura

| VM | Hostname | IP Host-Only | Rol |
|---|---|---|---|
| Nodo Control | nodocontrol | 192.168.56.10 | Ansible (no forma parte del Swarm) |
| Swarm Manager | swarm-manager | 192.168.56.11 | Manager del clúster |
| Worker 1 | worker-1 | 192.168.56.12 | Worker |
| Worker 2 | worker-2 | 192.168.56.13 | Worker |

## Stack desplegado

- **web** — Aplicación Flask con contador de visitas compartido · 3 réplicas · puerto 80
- **db** — Redis · 1 réplica · puerto 6379
- **visualizer** — Docker Visualizer · 1 réplica · puerto 8080

## Estructura del repositorio
