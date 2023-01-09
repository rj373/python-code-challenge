"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature<800 and neutrons_emitted>500 and temperature * neutrons_emitted < 500000):
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power=voltage*current
    a=(generated_power/theoretical_max_power)*100
    if a>=80.00:
        return 'green'
    elif a<80.00 and a>=60.00:
        return 'orange'
    elif a<60.00 and a>=30.00:
        return 'red'
    else:
        return 'black'
        
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    criticality=temperature*neutrons_produced_per_second
    if criticality<0.9*threshold:
        return 'LOW'
    elif (threshold - 0.1 * threshold) <= criticality <= (threshold + 0.1 * threshold):
        return 'NORMAL'
    else:
        return 'DANGER'
