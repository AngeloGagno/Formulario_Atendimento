import streamlit as st
import pandas as pd
from backend.crud import CRUD

class AtendimentoApp:
    """
    Classe principal da aplicação Streamlit para gerenciamento de atendimentos.
    Implementa interface para todas as operações CRUD.
    """
    def __init__(self):
        self.crud = CRUD()
        self.setup_page()
        self.menu_options = {
            "Visualizar Atendimentos": self.view_page,
            "Criar Atendimento": self.create_page,
            "Atualizar Atendimento": self.update_page,
            "Excluir Atendimento": self.delete_page
        }

    def setup_page(self):
        """Configuração inicial da página."""
        st.set_page_config(page_title="Sistema de Atendimentos", layout="wide")
        st.title("Sistema de Gerenciamento de Atendimentos")

    def run(self):
        """Executa a aplicação principal."""
        # Sidebar para navegação
        st.sidebar.title("Navegação")
        opcao = st.sidebar.radio(
            "Selecione uma opção:",
            list(self.menu_options.keys())
        )
        
        # Renderiza a página selecionada
        self.menu_options[opcao]()

    def get_service_fields(self):
        """
        Retorna os campos da tabela Atendimentos baseado na classe definida.
        """
        return ["motivo", "canal", "origem", "gravidade"]

    def display_form(self, fields, valores_pre_preenchidos=None):
        """
        Exibe um formulário dinâmico baseado nos campos fornecidos.
        Retorna um dicionário com os dados preenchidos.
        """
        dados = {}
        for field in fields:
            # Adapte os tipos de input de acordo com o tipo dos campos
            if field == "gravidade":
                # Campo de gravidade é um inteiro de 1 a 5
                valores_pre = valores_pre_preenchidos.get(field, 1) if valores_pre_preenchidos else 1
                dados[field] = st.slider(f"{field.capitalize()}", 1, 5, valores_pre)
            elif field == "canal":
                opcoes = ["Email", "Telefone", "WhatsApp", "Presencial", "Outro"]
                if valores_pre_preenchidos and field in valores_pre_preenchidos:
                    index = opcoes.index(valores_pre_preenchidos[field]) if valores_pre_preenchidos[field] in opcoes else 0
                    dados[field] = st.selectbox(f"{field.capitalize()}", opcoes, index=index)
                else:
                    dados[field] = st.selectbox(f"{field.capitalize()}", opcoes)
            elif field == "origem":
                opcoes = ["Interno", "Externo", "Site", "Redes Sociais", "Outro"]
                if valores_pre_preenchidos and field in valores_pre_preenchidos:
                    index = opcoes.index(valores_pre_preenchidos[field]) if valores_pre_preenchidos[field] in opcoes else 0
                    dados[field] = st.selectbox(f"{field.capitalize()}", opcoes, index=index)
                else:
                    dados[field] = st.selectbox(f"{field.capitalize()}", opcoes)
            else:
                # Para o campo motivo, usamos uma área de texto
                if field == "motivo":
                    if valores_pre_preenchidos and field in valores_pre_preenchidos:
                        dados[field] = st.text_area(f"{field.capitalize()}", value=valores_pre_preenchidos[field], height=100)
                    else:
                        dados[field] = st.text_area(f"{field.capitalize()}", height=100)
                else:
                    if valores_pre_preenchidos and field in valores_pre_preenchidos:
                        dados[field] = st.text_input(f"{field.capitalize()}", value=valores_pre_preenchidos[field])
                    else:
                        dados[field] = st.text_input(f"{field.capitalize()}")
        return dados

    def mostrar_tabela(self, services):
        """Exibe os dados dos atendimentos em formato de tabela."""
        if services:
            # Converte objetos para um DataFrame
            data_list = []
            for service in services:
                # Extrair os dados do objeto de forma segura
                service_dict = {
                    'id': getattr(service, 'id', None),
                    'motivo': getattr(service, 'motivo', ''),
                    'canal': getattr(service, 'canal', ''),
                    'origem': getattr(service, 'origem', ''),
                    'gravidade': getattr(service, 'gravidade', 0)
                }
                data_list.append(service_dict)
            
            df = pd.DataFrame(data_list)
            
            # Adiciona formatação condicional para o campo gravidade
            if 'gravidade' in df.columns:
                st.dataframe(
                    df,
                    column_config={
                        "gravidade": st.column_config.ProgressColumn(
                            "Gravidade",
                            help="Nível de gravidade do atendimento (1-5)",
                            format="%d",
                            min_value=1,
                            max_value=5,
                        )
                    }
                )
            else:
                st.dataframe(df)
        else:
            st.info("Não há atendimentos registrados.")

    def view_page(self):
        """Página para visualizar atendimentos."""
        st.header("Visualizar Atendimentos")
        
        visualizar_opcao = st.radio("Escolha a opção de visualização:", 
                                    ["Todos os Atendimentos", "Atendimento Específico"])
        
        if visualizar_opcao == "Todos os Atendimentos":
            services = self.crud.read_all_services()
            self.mostrar_tabela(services)
        else:
            service_id = st.number_input("Digite o ID do atendimento", min_value=1, step=1)
            if st.button("Buscar"):
                try:
                    service = self.crud.read_a_service(service_id)
                    self.mostrar_tabela([service])
                except IndexError:
                    st.error(f"Atendimento com ID {service_id} não encontrado.")
                except Exception as e:
                    st.error(f"Erro ao buscar o atendimento: {e}")

    def create_page(self):
        """Página para criar novos atendimentos."""
        st.header("Criar Novo Atendimento")
        
        # Verificar se há uma flag de sucesso
        if 'create_success' in st.session_state:
            st.success("Atendimento criado com sucesso!")
            # Limpar a flag após exibir
            del st.session_state['create_success']
            
        fields = self.get_service_fields()
        dados = self.display_form(fields)
        
        if st.button("Criar Atendimento"):
            try:
                # Validação do formulário
                if not dados["motivo"]:
                    st.warning("O campo Motivo é obrigatório.")
                    return
                
                # Assegura que a gravidade seja um inteiro
                if "gravidade" in dados:
                    dados["gravidade"] = int(dados["gravidade"])
                
                self.crud.create_service(**dados)
                
                # Definir flag de sucesso e limpar formulário
                st.session_state['create_success'] = True
                st.rerun()
                
            except Exception as e:
                st.error(f"Erro ao criar o atendimento: {e}")

    def update_page(self):
        """Página para atualizar atendimentos existentes."""
        st.header("Atualizar Atendimento")
        
        # Verificar se há uma flag de sucesso
        if 'update_success' in st.session_state:
            st.success("Atendimento atualizado com sucesso!")
            # Limpar a flag após exibir
            del st.session_state['update_success']
        
        # Primeiro, selecionar o atendimento a ser atualizado
        service_id = st.number_input("Digite o ID do atendimento a ser atualizado", min_value=1, step=1)
        
        if st.button("Buscar para Atualizar"):
            try:
                service = self.crud.read_a_service(service_id)
                
                # Em vez de armazenar o objeto completo, armazenamos apenas os dados
                service_data = {
                    'id': getattr(service, 'id', None),
                    'motivo': getattr(service, 'motivo', ''),
                    'canal': getattr(service, 'canal', ''),
                    'origem': getattr(service, 'origem', ''),
                    'gravidade': getattr(service, 'gravidade', 0)
                }
                
                st.session_state['service_to_update_data'] = service_data
                st.success(f"Atendimento ID {service_id} encontrado. Atualize os campos abaixo.")
            except IndexError:
                st.error(f"Atendimento com ID {service_id} não encontrado.")
            except Exception as e:
                st.error(f"Erro ao buscar o atendimento: {e}")
        
        # Se um atendimento foi selecionado, mostra os campos para atualização
        if 'service_to_update_data' in st.session_state:
            service_data = st.session_state['service_to_update_data']
            st.subheader(f"Atualizar Atendimento ID: {service_data['id']}")
            
            # Remove o ID que não deve ser atualizado
            update_data = {k: v for k, v in service_data.items() if k != 'id'}
            
            # Exibe formulário com valores pré-preenchidos
            fields = self.get_service_fields()
            dados_atualizados = self.display_form(fields, update_data)
            
            col1, col2 = st.columns([1, 3])
            
            with col1:
                if st.button("Salvar Alterações", type="primary", use_container_width=True):
                    try:
                        # Validação do formulário
                        if not dados_atualizados["motivo"]:
                            st.warning("O campo Motivo é obrigatório.")
                            return
                        
                        # Assegura que a gravidade seja um inteiro
                        if "gravidade" in dados_atualizados:
                            dados_atualizados["gravidade"] = int(dados_atualizados["gravidade"])
                        
                        # Remove campos vazios e filtra para incluir apenas os que foram alterados
                        dados_alterados = {k: v for k, v in dados_atualizados.items() 
                                        if v and k in update_data and str(v) != str(update_data[k])}
                        
                        if dados_alterados:
                            self.crud.update_service(service_data['id'], **dados_alterados)
                            
                            # Definir flag de sucesso e limpar seleção
                            st.session_state['update_success'] = True
                            del st.session_state['service_to_update_data']
                            st.rerun()
                        else:
                            st.info("Nenhuma alteração detectada.")
                    except Exception as e:
                        st.error(f"Erro ao atualizar o atendimento: {e}")
            
            with col2:
                if st.button("Cancelar", use_container_width=True):
                    del st.session_state['service_to_update_data']
                    st.rerun()

    def delete_page(self):
        """Página para excluir atendimentos."""
        st.header("Excluir Atendimento")
        
        # Verificar se há uma flag de sucesso
        if 'delete_success' in st.session_state:
            st.success(f"Atendimento excluído com sucesso!")
            # Limpar a flag após exibir
            del st.session_state['delete_success']
        
        service_id = st.number_input("Digite o ID do atendimento a ser excluído", min_value=1, step=1)
        
        # Adiciona uma confirmação para evitar exclusões acidentais
        if st.button("Buscar para Excluir"):
            try:
                service = self.crud.read_a_service(service_id)
                
                # Em vez de armazenar o objeto completo, armazenamos apenas os dados
                service_data = {
                    'id': getattr(service, 'id', None),
                    'motivo': getattr(service, 'motivo', ''),
                    'canal': getattr(service, 'canal', ''),
                    'origem': getattr(service, 'origem', ''),
                    'gravidade': getattr(service, 'gravidade', 0)
                }
                
                st.session_state['service_to_delete_data'] = service_data
                
                # Mostra os dados do atendimento
                st.subheader("Dados do Atendimento:")
                
                # Criar um DataFrame para exibição mais limpa
                df = pd.DataFrame([service_data])
                st.dataframe(df)
                
                st.warning("Tem certeza que deseja excluir este atendimento? Esta ação não pode ser desfeita.")
            except IndexError:
                st.error(f"Atendimento com ID {service_id} não encontrado.")
            except Exception as e:
                st.error(f"Erro ao buscar o atendimento: {e}")
        
        # Se um atendimento foi selecionado para exclusão
        if 'service_to_delete_data' in st.session_state:
            service_data = st.session_state['service_to_delete_data']
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("Confirmar Exclusão", type="primary", use_container_width=True):
                    try:
                        # Excluir o atendimento usando o ID armazenado
                        self.crud.delete_service(service_data['id'])
                        
                        # Definir flag de sucesso e limpar seleção
                        st.session_state['delete_success'] = True
                        del st.session_state['service_to_delete_data']
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao excluir o atendimento: {e}")
            with col2:
                if st.button("Cancelar", use_container_width=True):
                    del st.session_state['service_to_delete_data']
                    st.rerun()