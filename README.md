Carrefour BDD Automation Framework

Site-ul testat: www.carrefour.ro
Design pattern-ul folosit: Page Object Model
Metodologia: Behavior Driven Development

1.	Instalați Google Chrome
2.	Instalați Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
3.	Instalați Python https://www.python.org/downloads/

Pentru a clona/importa proiectul:
1.	Descărcați GIT: https://git-scm.com/downloads
2.	Deschideți folderul unde doriți să clonați proiectul, dați click dreapta, selectați ”Git Bash Here”
3.	In fereastra deschisă, dați „paste” la urmatorea comandă:
git clone https://github.com/AlexandraBalau/Carrefour_BDD_Automation_Framework.git

Libraries to install:
pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager

În Terminal, run tests:

behave -f html -o behave-report.html

Troubleshoot:
a.
Daca nu funcționează cu pip încercați comanda: py -m pip install selenium

b.
Dacă nici așa nu reusiți:
File -> Settings -> Click pe Project: [nume_proiect] -> Python Interpreter -> +
Cautati 'selenium' -> Install Package
La fel si pentru restul librăriilor.

c.
Click pe tabul de jos 'Python Packages' din consolă.
Căutati și instalați pachetele de mai sus.
