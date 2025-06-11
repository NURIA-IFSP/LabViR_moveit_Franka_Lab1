# Laboratório Virtual de RObótica - Ambiente ROS Noetic

Este é o ambiente de desenvolvimento do LabVir com o ROS 1 - noetic

Os pacotes instalados são:


# Pacotes ROS 1 Noetic Instalados

## Ferramentas Essenciais
- `git` e `nano`: Versionamento e editor de texto básico
- `python-is-python3`: Garante compatibilidade com Python 3 (padrão no ROS Noetic)
- `python3-catkin-tools` e `ros-noetic-catkin`: Ferramentas para compilação de workspace ROS

## Pacotes Básicos ROS
- `ros-noetic-ros-tutorials`: Tutoriais oficiais ROS (pacotes de exemplo)
- `ros-noetic-serial`: Comunicação serial com dispositivos externos

## Simulação e Visualização
- `ros-noetic-gazebo-ros-pkgs`: Integração entre ROS e Gazebo
- `ros-noetic-gazebo-ros-control`: Plugins de controle para simulação no Gazebo
- `ros-noetic-rviz-visual-tools`: Ferramentas visuais para RVIZ
- `liburdfdom-tools`: Utilitários para trabalhar com arquivos URDF (modelos de robôs)

## Controle de Robôs
- `ros-noetic-ros-control`: Framework padrão para controle de robôs
- `ros-noetic-ros-controllers`: Controladores ROS pré-implementados
- `ros-noetic-effort-controllers`: Controladores para joints com esforço/torque
- `ros-noetic-rqt-joint-trajectory-controller`: Interface RQT para controladores de trajetória

## Movimento e Planejamento
- `ros-noetic-moveit`: Framework completo para movimento e manipulação robótica

## Dependências Adicionais
- `libpoco-dev`: Bibliotecas para desenvolvimento de redes
- `python3-wstool`: Ferramenta para gerenciamento de workspaces ROS

> **Nota**: Esta combinação de pacotes é ideal para desenvolvimento com:
> - Simulação no Gazebo
> - Controle de robôs reais
> - Aplicações de manipulação robótica
> - Visualização avançada no RVIZ

---


# Como executar:

Você pode executar em sua máquina local ou via GitHub Codespaces. Se for executar no seu computador é necessária a preparação do ambiente local, caso contrário vá para a seção ["Tutorial Via GitHub Codespaces"](#tutorial-via-github-codespaces).

## Preparação do ambiente na máquina local - git + docker + vscode

1. Verifique se o git está instalado

    ```bash
    git --version
    ```

    1.1 - Se não estiver instalar:

    ```bash
    sudo apt install git
    ```

2. Baixar o repositorio em sua máquina local:

    ```bash
    git clone https://github.com/NURIA-IFSP/LabVir_noetic_lab.git
    ```

3. Abrir o vscode no diretório do projeto:

    ```bash
    code LabVir_noetic_lab
    ```

4. Garanta que o docker esteja instalado e rodando:

    ```bash
        docker --version
    ```

5. Se não tiver, instalar o docker:

    [Docker Installation Guide](https://docs.docker.com/get-started/get-docker/)

6. Instale a extensão remote - developement: workspace, no vscode:

    - No menu de extensões do VsCode Ctrl + Shift + X procure por: Remote - Development: Workspace

## Execução do container no vscode

1. Clique no botão de play no canto inferior esquerdo do vscode:
    ![image](./images/readme/vscode_open_remotel.png)

2. Clique em "Reopen in Container"

3. Aguarde o container ser iniciado, o vscode irá reiniciar e abrir novamente. (Isso deve levar alguns minutos)

## Abra o ambiente de desenvolvimento no seu browser

1. Abra o terminal PORTS do vscode com o atalho: Ctrl + Shift + P - Forward a Port

2. Clique na primeira porta que estará mapeada no endereço:  <http://localhost:6080>

3. O ambiente XFCE4 deverá abrir no seu browser

4. Se desejar, ajuste a resolução para o seu monitor clicando no canto superior esquerdo do ambiente XFCE4 e selecionando "Display Settings"

5. Clique no botão para estender a exibição para a tela inteira - atalho: Ctrl + Shift + F12

## Execução Via GitHub Codespaces

Na execução via github Codespaces você não precisará instalar nada em seu computador, terá apenas que ter uma conta no github.

1. Acesse o repositório do projeto no github:
    [https://github.com/NURIA-IFSP/LabVir_noetic_lab](https://github.com/NURIA-IFSP/LabVir_noetic_lab)
    - Clique no botão "Code" e selecione "Codespaces"
    - O ambiente começará a ser montado no Codespaces (isso pode levar alguns minutos)

2. Feito isso abra o ambiente de desenvolvimento no seu browser, conforme explicado anteriormente e siga os mesmos passos.

3. Avisos Importantes para simulação usando Codespaces:
    - Após a execução do ambiente você deverá clicar no botão "Stop" para encerrar o ambiente.
    - A execução de ambientes de desenvolvimento é cobrada pelo github, havendo um limite atual de 60 horas de execução por mês, ou 180 horas por mês para usuários com acesso premium. Estudantes e professores podem ter o limite aumentado.
