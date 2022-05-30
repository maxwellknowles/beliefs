## Imports
import streamlit as st
import graphviz as graphviz

st.set_page_config(page_title="The Belief Flow", page_icon=":heart:", layout="wide",initial_sidebar_state="expanded")
st.header("Belief Flow")
# Create a graphlib graph object
graph = graphviz.Digraph()

#questions of origins
universe = st.selectbox('Does the universe have a beginning?',('Yes', 'No'))
multiverse = st.selectbox('Do you believe there are multiple universes or the death of a universe led to the creation of our own?',('No','Yes'))
simulation_theory = st.selectbox('Do you believe we are in a simulation and there are potentially many or multiple layers of simulations?',('No','Yes'))
life_complexity = st.selectbox('Do you acknowledge the incredible improbability of human consciousness emerging?',('Yes','No'))
#questions of value
human_value_why = st.selectbox("Is a person valuable (and deserving of rights) innately or because the state says so?",('Innate Value','The State'))
if human_value_why == 'Innate Value':
    human_value_innate_why = st.selectbox("Why does a person have innate value?", ("Because they are unique, conscious beings", "Because they were created","Just because"))
caring = st.selectbox("Do we have a moral responsibility to uphold the value of fellow humans?", ("Yes", "No"))
lottery = st.selectbox("How much control did you have over where and when you were born?", ("No control", "I could influence my own birth"))

#policy implications of value
lottery2 = st.selectbox("Should people's life outcomes be constrained by their place of birth?", ("No", "Yes"))
action = st.selectbox("Does minimizing chance in life outcomes require some form of action or support from others?", ("Yes", "No"))
if action == "Yes":
    choice = st.selectbox("How much should helping to improve life outcomes be a personal choice versus a group choice?", ("Personal", "Group"))
    if choice == "Personal":
        personal = st.selectbox("Is it okay to make personal choices that don't improve the life outcomes of others?", ("No", "Yes"))
    if choice == "Group":
        group = st.selectbox("How does a group best determine how to make decisions?", ("Democracy", "Rule of those in power"))
killing = st.selectbox("Is killing a human wrong?", ("Yes", "No"))
if killing == "Yes":
    killing_why = st.selectbox("What makes killing wrong? What makes death sad or a loss?", ("It eliminates the critically high potential of future life", "It eliminates a life that has experienced conscious thought, memories, relationships, etc", "Both"))
    abortion = st.selectbox("Are you pro-life or pro-choice?", ("Pro-life", "Pro-choice"))
healthcare = st.selectbox("Everyone should have access to the healthcare they need?", ("Yes", "No"))
environment = st.selectbox("Should we embrace sustainable policies?", ("Yes", "No"))

#origins and nature of existence
if universe == 'No':
    graph.edge('The universe does not have an origin', 'LOGIC BREAK')

if universe == 'Yes':
    graph.edge('The universe has an origin', 'A creative agent exists (a deity, simulator, natural phenomenon, etc)')

if multiverse == "Yes" or simulation_theory == "Yes":
    graph.edge("The multiverse or simulation theory increase complexity of existence", 'The necessity of a creative agent of intelligence increases')
    graph.edge('The necessity of a creative agent of intelligence increases', 'A creative agent exists (a deity, simulator, natural phenomenon, etc)')

if life_complexity == 'Yes':
    graph.edge('A creative agent exists (a deity, simulator, natural phenomenon, etc)', "The probability of human consciousness emerging is extraordinarily low")
    graph.edge("The probability of human consciousness emerging is extraordinarily low", "Human consciousness is likely an intentional result of life's processes")
    graph.edge("Human consciousness is likely an intentional result of life's processes", "A creative agent was intentional about human consciousness developing")

#basis of human value
if human_value_why == 'The State':
    graph.edge('Human value and rights are derived from the state', "Human value is defined by who is in power and morality is relative")
    if life_complexity == "Yes":
        graph.edge("A creative agent was intentional about human consciousness developing", "Human value and rights (the basis of morality) is the product of a creative agent")
        graph.edge("A creative agent was intentional about human consciousness developing", 'Human value and rights are derived from the state', 'LOGIC BREAK')
    if caring == "Yes":
        graph.edge("Human value is defined by who is in power and morality is relative", "We have a moral obligation to care for others", "LOGIC BREAK")

    if caring == "No":
        graph.edge("Human value is defined by who is in power and morality is relative", "We don't have a moral obligation to care for others")

if human_value_why == 'Innate Value':
    if human_value_innate_why == "Because they are unique, conscious beings":
        graph.edge("A creative agent was intentional about human consciousness developing", "Human value and rights (the basis of morality) is the product of a creative agent")
        graph.edge("Unique human consciousness engenders a person with innate value and rights", "Human value and rights (the basis of morality) is the product of a creative agent")
        graph.edge('A creative agent exists (a deity, simulator, natural phenomenon, etc)',"Human value and rights (the basis of morality) is the product of a creative agent")
        graph.edge("A creative agent was intentional about human consciousness developing", "A creative agent that planned for consciousness intentionally was or is likely a conscious being")
        graph.edge("A creative agent that planned for consciousness intentionally was or is likely a conscious being", "The creative agent is likely an intentional, powerful, sentient, conscious being")        
        graph.edge("Human value and rights (the basis of morality) is the product of a creative agent", "The creative agent is likely an intentional, powerful, sentient, conscious being") 

        if caring == "Yes":
            graph.edge("A creative agent was intentional about human consciousness developing", "Unique human consciousness engenders a person with innate value and rights")
            graph.edge("Unique human consciousness engenders a person with innate value and rights", "We have a moral obligation to care for others")

        if caring == "No":
            graph.edge("A creative agent was intentional about human consciousness developing", "Unique human consciousness engenders a person with innate value and rights")
            graph.edge("Unique human consciousness engenders a person with innate value and rights", "We don't have a moral obligation to care for others", "LOGIC BREAK")

    if human_value_innate_why == "Because they were created":
        if caring == "Yes":
            graph.edge("A creative agent was intentional about human consciousness developing", "Human value and rights (the basis of morality) is the product of a creative agent")
            graph.edge("Human value and rights (the basis of morality) is the product of a creative agent", "We have a moral obligation to care for others")
        if caring == "No":
            graph.edge("A creative agent was intentional about human consciousness developing", "Human value and rights (the basis of morality) is the product of a creative agent")
            graph.edge("Human value and rights (the basis of morality) is the product of a creative agent", "We don't have a moral obligation to care for others", "LOGIC BREAK")

    if human_value_innate_why == "Just because":
        graph.edge("A person is valuable innately but without a foundational reason", "LOGIC BREAK")

        if caring == "Yes":
            graph.edge("Humans possess innate value", "We have a moral obligation to care for others")
        if caring == "No":
            graph.edge("Humans possess innate value", "We don't have a moral obligation to care for others", "LOGIC BREAK")

#implications of human value
if caring == "Yes":
    if lottery == "I could influence my own birth":
        graph.edge("I could influence my own birth", "LOGIC BREAK")
    if lottery == "No control":
        graph.edge("We don't have any influence on when and where we were born", "The family, money, education, religion, and politics we were raised with was not by our own choice")
        graph.edge("We don't have any influence on when and where we were born", "We are all equal")
        if lottery2 == "Yes":
            graph.edge("We have a moral obligation to care for others", "We should try to limit the role of chance in limiting life outcomes")
            graph.edge("The family, money, education, religion, and politics we were raised with was not by our own choice", "Despite the lack of choice involved, this should determine life outcomes", "LOGIC BREAK")
            if action == "Yes":
                graph.edge("Despite the lack of choice involved, this should determine life outcomes", "We should try to limit the role of chance in limiting life outcomes", "LOGIC BREAK")
                graph.edge("We should try to limit the role of chance in limiting life outcomes", "We will need to sacrifice money, time, or materials to improve society")
                if choice == "Personal":
                    graph.edge("We will need to sacrifice money, time, or materials to improve society", "Improving others' life outcomes should be done as a personal choice")
                    if personal == "Yes":
                        graph.edge("Improving others' life outcomes should be done as a personal choice", "We don't have an obligation to do this", "LOGIC BREAK")
                    if personal == "No":
                        graph.edge("Improving others' life outcomes should be done as a personal choice", "We have an obligation to do this")
                if choice == "Group":
                    graph.edge("We will need to sacrifice money, time, or materials to improve society", "Improving others' life outcomes should be done as a group")
                    if group == "Democracy":
                        graph.edge("Improving others' life outcomes should be done as a group", "The group should vote on this process")
                        graph.edge("We are all equal", "The group should vote on this process")
                    if group == "Rule of those in power":
                        graph.edge("Improving others' life outcomes should be done as a group", "The group should be guided by those in power")
                        graph.edge("We are all equal", "The group should be guided by those in power", "LOGIC BREAK")
            if action == "No":
                graph.edge("Despite the lack of choice involved, this should determine life outcomes", "We will not need to sacrifice money, time, or materials to improve society")
        if lottery2 == "No":
            graph.edge("We have a moral obligation to care for others", "We should try to limit the role of chance in limiting life outcomes")
            graph.edge("The family, money, education, religion, and politics we were raised with was not by our own choice", "We should try to limit the role of chance in limiting life outcomes")
            if action == "Yes":
                graph.edge("We should try to limit the role of chance in limiting life outcomes", "We will need to sacrifice money, time, or materials to improve society")
                if choice == "Personal":
                    graph.edge("We will need to sacrifice money, time, or materials to improve society", "Improving others' life outcomes should be done as a personal choice")
                    if personal == "Yes":
                        graph.edge("Improving others' life outcomes should be done as a personal choice", "We don't have an obligation to do this", "LOGIC BREAK")
                    if personal == "No":
                        graph.edge("Improving others' life outcomes should be done as a personal choice", "We have an obligation to do this")
                if choice == "Group":
                    graph.edge("We will need to sacrifice money, time, or materials to improve society", "Improving others' life outcomes should be done as a group")
                    if group == "Democracy":
                        graph.edge("Improving others' life outcomes should be done as a group", "The group should vote on this process")
                        graph.edge("We are all equal", "The group should vote on this process")
                    if group == "Rule of those in power":
                        graph.edge("Improving others' life outcomes should be done as a group", "The group should be guided by those in power")
                        graph.edge("We are all equal", "The group should be guided by those in power", "LOGIC BREAK")
            if action == "No":
                graph.edge("We should try to limit the role of chance in limiting life outcomes", "We will not need to sacrifice money, time, or materials to improve society", "LOGIC BREAK")

        if environment == "Yes":
            graph.edge("We should try to limit the role of chance in limiting life outcomes", "We should embrace sustainability to support life across time and location")
        
        if environment == "No":
            graph.edge("We should try to limit the role of chance in limiting life outcomes", "We should not embrace sustainability to support life across time and location", "LOGIC BREAK")

    if killing == "No":
        graph.edge("We have a moral obligation to care for others", "Killing isn't wrong, death isn't a loss", "LOGIC BREAK")

    if killing == "Yes":
        graph.edge("We have a moral obligation to care for others", "Killing is wrong")

        if killing_why == "It eliminates the critically high potential of future life":
            graph.edge("Killing is wrong","The potential good of life is what makes killing wrong")
            graph.edge("The potential good of life is what makes killing wrong", "Preventing a probable future life is wrong")
            if abortion == "Pro-life":
                graph.edge("Preventing a probable future life is wrong", "Pro-life policies")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-life policies")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We have a moral obligation to care for others", "The group should vote on this process", "LOGIC BREAK")
                            graph.edge("The group should vote on this process", "Pro-life policies")
                        if group == "Rule of those in power":
                            graph.edge("We have a moral obligation to care for others", "The group should be guided by those in power", "LOGIC BREAK")
                            graph.edge("The group should be guided by those in power", "Pro-life policies")
            if abortion == "Pro-choice":
                graph.edge("Preventing a probable future life is wrong", "Pro-choice policies", "LOGIC BREAK")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-choice policies")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-choice policies", "LOGIC BREAK")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We have a moral obligation to care for others", "The group should vote on this process", "LOGIC BREAK")
                            graph.edge("The group should vote on this process", "Pro-choice policies")
                        if group == "Rule of those in power":
                            graph.edge("We have a moral obligation to care for others", "The group should be guided by those in power", "LOGIC BREAK")
                            graph.edge("The group should be guided by those in power", "Pro-choice policies")
        if killing_why == "It eliminates a life that has experienced conscious thought, memories, relationships, etc":
            graph.edge("Killing is wrong","The loss of a known, conscious being is what makes killing wrong")
            graph.edge("The loss of a known, conscious being is what makes killing wrong", "Preventing people who've begun making memories and building relationships is important")
            if abortion == "Pro-life":
                graph.edge("Preventing people who've begun making memories and building relationships is important", "Pro-life policies", "LOGIC BREAK")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We have a moral obligation to care for others", "The group should vote on this process", "LOGIC BREAK")
                            graph.edge("The group should vote on this process", "Pro-life policies")
                        if group == "Rule of those in power":
                            graph.edge("We have a moral obligation to care for others", "The group should be guided by those in power", "LOGIC BREAK")
                            graph.edge("The group should be guided by those in power", "Pro-life policies")
            if abortion == "Pro-choice":
                graph.edge("Preventing people who've begun making memories and building relationships is important", "Pro-choice policies")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-choice policies")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-choice policies")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We have a moral obligation to care for others", "The group should vote on this process", "LOGIC BREAK")
                            graph.edge("The group should vote on this process", "Pro-choice policies")
                        if group == "Rule of those in power":
                            graph.edge("We have a moral obligation to care for others", "The group should be guided by those in power", "LOGIC BREAK")
                            graph.edge("The group should be guided by those in power", "Pro-choice policies")
        if killing_why == "Both":
            graph.edge("Killing is wrong", "The loss of future life and loss of an experienced life are what make killing wrong, death sad")
            graph.edge("The loss of future life and loss of an experienced life are what make killing wrong, death sad", "Protecting lives yet lived and that have been lived is important")
            if abortion == "Pro-life":
                graph.edge("Protecting lives yet lived and that have been lived is important", "Pro-life policies", "What makes killing wrong or death sad is protected")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-life policies")
                if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We have a moral obligation to care for others", "The group should vote on this process", "LOGIC BREAK")
                            graph.edge("The group should vote on this process", "Pro-life policies")
                        if group == "Rule of those in power":
                            graph.edge("We have a moral obligation to care for others", "The group should be guided by those in power", "LOGIC BREAK")
                            graph.edge("The group should be guided by those in power", "Pro-life policies")
            if abortion == "Pro-choice":
                graph.edge("Protecting lives yet lived and that have been lived is important", "Pro-choice policies", "What makes killing wrong or death sad isn't fully protected")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-choice policies")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-choice policies","LOGIC BREAK")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We have a moral obligation to care for others", "The group should vote on this process", "LOGIC BREAK")
                            graph.edge("The group should vote on this process", "Pro-choice policies")
                        if group == "Rule of those in power":
                            graph.edge("We have a moral obligation to care for others", "The group should be guided by those in power", "LOGIC BREAK")
                            graph.edge("The group should be guided by those in power", "Pro-choice policies")

    if healthcare == "Yes":
        graph.edge("We have a moral obligation to care for others", "People should have access to healthcare")

    if healthcare == "No":
        graph.edge("We have a moral obligation to care for others", "People should not have access to healthcare", "LOGIC BREAK")

if caring == "No":
    if lottery == "I could influence my own birth":
        graph.edge("I could influence my own birth", "LOGIC BREAK")
    if lottery == "No control":
        graph.edge("We don't have any influence on when and where we were born", "The family, money, education, religion, and politics we were raised with was not by our own choice")
        graph.edge("We don't have any influence on when and where we were born", "We are all equal")
        if lottery2 == "Yes":
            graph.edge("We don't have a moral obligation to care for others", "We should try to limit the role of chance in limiting life outcomes", "LOGIC BREAK")
            graph.edge("The family, money, education, religion, and politics we were raised with was not by our own choice", "Despite the lack of choice involved, this should determine life outcomes")
        if lottery2 == "No":
            graph.edge("We don't have a moral obligation to care for others", "We should try to limit the role of chance in limiting life outcomes", "LOGIC BREAK")
            graph.edge("The family, money, education, religion, and politics we were raised with was not by our own choice", "We should try to limit the role of chance in limiting life outcomes", "LOGIC BREAK")
            if action == "Yes":
                graph.edge("We should try to limit the role of chance in limiting life outcomes", "We will need to sacrifice money, time, or materials to improve society")
                if choice == "Personal":
                    graph.edge("We will need to sacrifice money, time, or materials to improve society", "Improving others' life outcomes should be done as a personal choice")
                    if personal == "Yes":
                        graph.edge("Improving others' life outcomes should be done as a personal choice", "We don't have an obligation to do this", "LOGIC BREAK")
                    if personal == "No":
                        graph.edge("Improving others' life outcomes should be done as a personal choice", "We have an obligation to do this")
                if choice == "Group":
                    graph.edge("We will need to sacrifice money, time, or materials to improve society", "Improving others' life outcomes should be done as a group")
                    if group == "Democracy":
                        graph.edge("Improving others' life outcomes should be done as a group", "The group should vote on this process")
                        graph.edge("We are all equal", "The group should vote on this process")
                    if group == "Rule of those in power":
                        graph.edge("Improving others' life outcomes should be done as a group", "The group should be guided by those in power")
                        graph.edge("We are all equal", "The group should be guided by those in power", "LOGIC BREAK")
            if action == "No":
                graph.edge("We should try to limit the role of chance in limiting life outcomes", "We will not need to sacrifice money, time, or materials to improve society", "LOGIC BREAK")
    
        if environment == "Yes":
            graph.edge("We don't have a moral obligation to care for others", "We should embrace sustainability to support life across time and location", "LOGIC BREAK")
        
        if environment == "No":
            graph.edge("We don't have a moral obligation to care for others", "We should not embrace sustainability to support life across time and location")

    if killing == "No":
        graph.edge("We don't have a moral obligation to care for others", "Killing isn't wrong, death isn't a loss")

    if killing == "Yes":
        graph.edge("We don't have a moral obligation to care for others", "Killing is wrong", "LOGIC BREAK")

        if killing_why == "It eliminates the critically high potential of future life":
            graph.edge("Killing is wrong","The potential good of life is what makes killing wrong")
            graph.edge("The potential good of life is what makes killing wrong", "Preventing a probable future life is wrong")
            if abortion == "Pro-life":
                graph.edge("Preventing a probable future life is wrong", "Pro-life policies")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-life policies")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We don't have a moral obligation to care for others", "The group should vote on this process")
                            graph.edge("The group should vote on this process", "Pro-life policies")
                        if group == "Rule of those in power":
                            graph.edge("We don't have a moral obligation to care for others", "The group should be guided by those in power")
                            graph.edge("The group should be guided by those in power", "Pro-life policies")
            if abortion == "Pro-choice":
                graph.edge("Preventing a probable future life is wrong", "Pro-choice policies", "LOGIC BREAK")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-choice policies")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-choice policies", "LOGIC BREAK")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We don't have a moral obligation to care for others", "The group should vote on this process")
                            graph.edge("The group should vote on this process", "Pro-choice policies")
                        if group == "Rule of those in power":
                            graph.edge("We don't have a moral obligation to care for others", "The group should be guided by those in power")
                            graph.edge("The group should be guided by those in power", "Pro-choice policies")
        if killing_why == "It eliminates a life that has experienced conscious thought, memories, relationships, etc":
            graph.edge("Killing is wrong","The loss of a known, conscious being is what makes killing wrong")
            graph.edge("The loss of a known, conscious being is what makes killing wrong", "Preventing people who've begun making memories and building relationships is important")
            if abortion == "Pro-life":
                graph.edge("Preventing people who've begun making memories and building relationships is important", "Pro-life policies", "LOGIC BREAK")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We don't have a moral obligation to care for others", "The group should vote on this process")
                            graph.edge("The group should vote on this process", "Pro-life policies")
                        if group == "Rule of those in power":
                            graph.edge("We don't have a moral obligation to care for others", "The group should be guided by those in power")
                            graph.edge("The group should be guided by those in power", "Pro-life policies")
            if abortion == "Pro-choice":
                graph.edge("Preventing people who've begun making memories and building relationships is important", "Pro-choice policies")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-choice policies")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-choice policies")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We don't have a moral obligation to care for others", "The group should vote on this process")
                            graph.edge("The group should vote on this process", "Pro-choice policies")
                        if group == "Rule of those in power":
                            graph.edge("We don't have a moral obligation to care for others", "The group should be guided by those in power")
                            graph.edge("The group should be guided by those in power", "Pro-choice policies")
        if killing_why == "Both":
            graph.edge("Killing is wrong", "The loss of future life and loss of an experienced life are what make killing wrong, death sad")
            graph.edge("The loss of future life and loss of an experienced life are what make killing wrong, death sad", "Protecting lives yet lived and that have been lived is important")
            if abortion == "Pro-life":
                graph.edge("Protecting lives yet lived and that have been lived is important", "Pro-life policies", "What makes killing wrong or death sad is protected")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-life policies", "LOGIC BREAK")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-life policies")
                if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We don't have a moral obligation to care for others", "The group should vote on this process")
                            graph.edge("The group should vote on this process", "Pro-life policies")
                        if group == "Rule of those in power":
                            graph.edge("We don't have a moral obligation to care for others", "The group should be guided by those in power")
                            graph.edge("The group should be guided by those in power", "Pro-life policies")
            if abortion == "Pro-choice":
                graph.edge("Protecting lives yet lived and that have been lived is important", "Pro-choice policies", "What makes killing wrong or death sad isn't fully protected")
                if action == "Yes":
                    if choice == "Personal":
                        if personal == "Yes":
                            graph.edge("We don't have an obligation to do this", "Pro-choice policies")
                        if personal == "No":
                            graph.edge("We have an obligation to do this", "Pro-choice policies","LOGIC BREAK")
                    if choice == "Group":
                        if group == "Democracy":
                            graph.edge("We don't have a moral obligation to care for others", "The group should vote on this process")
                            graph.edge("The group should vote on this process", "Pro-choice policies")
                        if group == "Rule of those in power":
                            graph.edge("We don't have a moral obligation to care for others", "The group should be guided by those in power")
                            graph.edge("The group should be guided by those in power", "Pro-choice policies")

    if healthcare == "Yes":
        graph.edge("We don't have a moral obligation to care for others", "People should have access to healthcare", "LOGIC BREAK")

    if healthcare == "No":
        graph.edge("We don't have a moral obligation to care for others", "People should not have access to healthcare")

st.graphviz_chart(graph, use_container_width=False)
