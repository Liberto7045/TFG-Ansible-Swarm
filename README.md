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

```
Nodo-Control/ansible_project/
├── deploy_swarm.yml        # Playbook principal (4 fases)
├── scale.yml               # Escalado dinámico de réplicas
├── restart_cluster.sh      # Script de recuperación post-suspensión
├── hosts                   # Inventario de nodos
└── roles/
    ├── docker_install/     # Instalación de Docker CE
    ├── swarm_init/         # Inicialización del Manager
    ├── swarm_join/         # Unión de Workers al clúster
    └── deploy_app/         # Despliegue del stack
```

## Requisitos previos

- 4 VMs con Ubuntu 24.04.4 LTS Server
- Ansible 2.16+ instalado en el Nodo Control
- Colección community.docker: `ansible-galaxy collection install community.docker`
- Acceso SSH sin contraseña desde el Nodo Control a los 3 nodos

## Uso

### Despliegue completo
```bash
ansible-playbook -i ~/ansible_project/hosts ~/ansible_project/deploy_swarm.yml
```

### Escalar réplicas
```bash
ansible-playbook -i ~/ansible_project/hosts ~/ansible_project/scale.yml -e "replicas=5"
```

### Recuperar el clúster tras suspensión de VMs
```bash
~/ansible_project/restart_cluster.sh
```

### Acceso a los servicios
- Aplicación web: `http://libertotfg.test` o `http://192.168.222.139`
- Visualizer: `http://192.168.222.139:8080`

## Tecnologías

Docker Swarm · Ansible 2.16 · Python Flask · Redis · Ubuntu 24.04 · VMware Workstation · dnsmasq · community.docker
