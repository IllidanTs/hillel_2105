class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_team_lead_attributes():
    team_lead = TeamLead("Alex", 100000, "IT", "Python", 5)
    assert hasattr(team_lead, 'name'), "Атрибут 'name' відсутній"
    assert hasattr(team_lead, 'salary'), "Атрибут 'salary' відсутній"
    assert hasattr(team_lead, 'department'), "Атрибут 'department' відсутній"
    assert hasattr(team_lead, 'programming_language'), "Атрибут 'programming_language' відсутній"
    assert hasattr(team_lead, 'team_size'), "Атрибут 'team_size' відсутній"
    print("Усі атрибути наявні!")

test_team_lead_attributes()
