# =====================================================
# Importando os módulos necessários
# =====================================================
import random

# =====================================================
# Comandos: Regras básicas
# =====================================================
def ord_atributos(param: str): #! STATUS: COMPLETO
    match param:
        case 'ajuda':
            return('Personagens de Ordem Paranormal RPG possuem cinco atributos, que definem suas competências básicas: Agilidade, Força, Intelecto, Presença e Vigor.')
        case 'agilidade':
            return(
                '- Define sua coordenação motora, velocidade de reação e destreza manual. Uma pessoa com Agilidade elevada é rápida e tem movimentos precisos, como um ginasta ou dançarino.\n'
                '- Agilidade é o atributo-base das perícias Acrobacia, Furtividade, Iniciativa, Crime, Pilotagem, Pontaria e Reflexos.'
            )
        case 'força':
            return(
                '- Determina sua potência muscular e habilidade atlética. Um personagem com Força alta tem grande capacidade física, seja por predisposição genética, treinamento constante ou modificação paranormal.\n'
                '- Força é o atributo-base de Atletismo e Luta, além de ser aplicada em suas rolagens de dano corpo a corpo e com armas de arremesso.'
            )
        case 'intelecto':
            return(
                '- Mede seu raciocínio, memória e educação geral. Uma pessoa com Intelecto elevado tem raciocínio rápido e afiado, conhecimento amplo sobre diversos assuntos e habilidades que envolvem estudo, como conhecimento científico.\n'
                '- Intelecto é o atributo-base de Atualidades, Ciências, Investigação, Medicina, Ocultismo, Profissão, Sobrevivência, Tática e Tecnologia.'
            )
        case 'presença':
            return(
                '- Define sua capacidade de observação, força de vontade e habilidades sociais. Um personagem com Presença alta é atento, determinado e possui boa lábia ou aparência. Pode ser uma figura agradável e descolada, ou séria e imponente.\n'
                '- Presença é o atributo-base de Diplomacia, Enganação, Intimidação, Intuição, Percepção, Religião e Vontade, além de conceder pontos de esforço adicionais por nível de exposição (NEX). Se você aumentar sua Presença, seus PE aumentam retroativamente.'
            )
        case 'vigor':
            return(
                '- Determina sua saúde e resistência física. Uma pessoa com Vigor elevado pode ser grande e robusta, ou simplesmente ter bom fôlego e disposição.\n'
                '- Vigor é o atributo-base de Fortitude, além de conceder pontos de vida adicionais por nível de exposição. Se você aumentar seu Vigor, seus PV aumentam retroativamente.'
            )

def ord_combate_acoes(param: str): #! STATUS: COMPLETO
    match param:
        case 'ajuda':
            return(
                '⁉️ | Em um turno você pode fazer: \n'
                '- Uma ação padrão e uma ação de movimento;\n'
                '- OU duas ações de movimento;\n'
                '- OU uma ação completa.'
                )
        case 'tipos':
            return('Os tipos de ação são: padrão, movimento, completa e livre.')
        case 'padrao' | 'padrão':
            return('Basicamente, uma ação padrão permite que você execute uma tarefa. Fazer um ataque ou conjurar um ritual são exemplos de ações padrão comuns.')
        case 'movimento':
            return('Esta ação representa algum tipo de movimento físico. Seu uso mais comum é percorrer uma distância igual ao seu deslocamento. Levantar-se, sacar uma arma, pegar um item de sua mochila, abrir uma porta e entrar em um carro também são ações de movimento.')
        case 'completa':
            return('Este tipo de ação exige todo o tempo e esforço normal de uma rodada. Para uma ação completa, você deve abrir mão de sua ação padrão e de sua ação de movimento — mas, normalmente, ainda pode realizar ações extras, ações livres e reações.')
        case 'livre':
            return('Esta ação não exige quase nenhum tempo e esforço, mas ainda só pode ser feita em seu turno. Jogar-se no chão ou gritar uma ordem são ações livres — mas o mestre pode decidir que algo é complicado demais para ser livre ou que uma determinada ação livre só pode ser feita uma vez por rodada. Dar uma ordem curta é uma ação livre; explicar um plano inteiro, não!')
        
def ord_classes(param: str):
    match param:
        case 'ajuda':
            return('Sua classe indica o treinamento que você recebeu na Ordem para enfrentar os perigos do Outro Lado. Em termos de jogo, é a sua característica mais importante, pois define o que você faz e qual é o seu papel no grupo de investigadores.')
        case 'tipos':
            return('Os tipos de classe são: combatente, especialista, ocultista e sobrevivente.')
        case 'combatente':
            return('Um perito em armas brancas e de fogo, este agente serve como a linha de frente na luta contra o Outro Lado. Jogue com um combatente se quiser ser perigoso e durão.')
        case 'especialista':
            return('Com conhecimento, esperteza e lábia, este agente é focado em resolver problemas diversos. Jogue com um especialista se quiser ser versátil e habilidoso.')
        case 'ocultista':
            return('Um estudioso do paranormal, que busca entender os mistérios dos elementos e usá-los a seu favor. Jogue com um ocultista se quiser dominar rituais e os poderes do Outro Lado — mas saiba que todo poder tem um preço.')
        case 'sobrevivente': #todo: fazer aqui com base no livro novo
            return('Em criação no sistema.')