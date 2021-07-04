from PyQt5 import QtCore, QtGui, QtWidgets

class Grafo:
    def __init__(self, vertices, direcionado=False):
        self.vertices = vertices ## Número de vértices do grafo
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] ## Criação do grafo em si
        self.direcionado = direcionado ## Variável para dizer se é direcionado

    def adiciona_aresta(self, u, v, peso=1):
        if self.direcionado:
            self.grafo[u-1][v-1] = peso
        else:
            self.grafo[u-1][v-1] = peso
            self.grafo[v-1][u-1] = peso

    ## Imprime a matriz de adjacências
    def mostra_matriz(self):
        ## Variável para ser retornada para a interface gráfica
        matriz_str = ''

        ## Contador
        c = 0

        ## Variável para imprimir os números ao redor da matriz
        vs = [i+1 for i in range(self.vertices)]
        vs = str(vs)
        vs = vs.replace('[', '')
        vs = vs.replace(']', '')

        # print(f'   {vs}')
        matriz_str += f'   {vs}'
        for i in range(self.vertices):

            # print(f'{c+1} ', end='')
            # print(self.grafo[i])

            matriz_str += '\n' + f'{c+1} '
            matriz_str += str(self.grafo[i])
            c += 1

        return matriz_str


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(836, 813)
        Form.setWindowIcon(QtGui.QIcon('grafos.png'))

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(590, 350, 163, 53))
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(80, 50, 588, 691))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 500))
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 6)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 5, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 6)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 10))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 6)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 4, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 2, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 2, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 2, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 2)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(80, 20, 331, 19))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.radioButton = QtWidgets.QRadioButton(self.widget1)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)


        self.pushButton.clicked.connect(self.adicionar_aresta)
        self.pushButton_2.clicked.connect(self.mostrar_grafo)
        self.pushButton_3.clicked.connect(self.remover_aresta)

        ## Guarda todos os vértices a serem adicionados ao grafo
        self.lista_final = []

        ## Guarda todos os vértices a serem adicionados ao grafo com 
        ## a finalidade de posteriormente ver qual dos vértices é o maior
        self.lista_maior = []

        ## Variável que vai guardar o maior dos vértices
        self.n = 0

        ##
        self.direcionado = False

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate(
            "Form", "Grafos - Matriz de Adjacência"))
        self.label_7.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", "O grafo será mostrado aqui"))
        self.pushButton_2.setText(_translate("Form", "Mostrar Grafo"))
        self.label_5.setText(_translate("Form", ""))
        self.label_8.setText(_translate("Form", "Peso (opcional, padrão = 1)"))
        self.label_6.setText(_translate("Form", "Lista de vértices adicionados:"))
        self.pushButton.setText(_translate("Form", "Adicionar Aresta"))
        self.label_3.setText(_translate("Form", "Vértice de Destino"))
        self.label_2.setText(_translate("Form", "Vértice de Origem"))
        self.pushButton_3.setText(_translate("Form", "Remover Aresta"))
        self.label_4.setText(_translate("Form", "Escolha o tipo do grafo"))
        self.radioButton.setText(_translate("Form", "Direcionado"))

    def adicionar_aresta(self):
        direcionado_local = self.direcionado
        direcionado_btn = self.radioButton.isChecked()

        ## Verifica se houve alguma mudança no tipo de Grafo
        if direcionado_local != direcionado_btn:
            self.lista_final.clear()

        self.direcionado = direcionado_btn
        
        ## Obter o vértice de origem e destino
        v_origem = int(self.lineEdit.text())
        v_destino = int(self.lineEdit_2.text())

        if self.lineEdit_3.text() != '':
            v_peso = int(self.lineEdit_3.text())
        else:
            v_peso = 1

        lista = [v_origem, v_destino, v_peso]

        self.lista_maior.append(v_origem)
        self.lista_maior.append(v_destino)
    
        self.lista_final.append(lista)

        ## Imprime na tela a lista de vértices ja adicionados
        self.label_5.setText(str(self.lista_final))

        ## Limpa os campos para uma nova inserção
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

        ## A medida que vai setando os vértices, também calcula o maior deles
        ## para posteriormente criar o grafo
        self.n = max(self.lista_maior)

    def remover_aresta(self):
        ## Mesma lógica da função de adicionar

        direcionado_local = self.direcionado
        direcionado_btn = self.radioButton.isChecked()

        if direcionado_local != direcionado_btn:
            self.lista_final.clear()

        v_origem = int(self.lineEdit.text())
        v_destino = int(self.lineEdit_2.text())

        if self.lineEdit_3.text() != '':
            v_peso = int(self.lineEdit_3.text())
        else:
            v_peso = 1

        lista = [v_origem, v_destino, v_peso]

        self.lista_maior.remove(v_origem)
        self.lista_maior.remove(v_destino)

        self.lista_final.remove(lista)
        self.label_5.setText(str(self.lista_final))

        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

        self.n = max(self.lista_maior)

    def mostrar_grafo(self):
        self.direcionado = False

        if self.radioButton.isChecked():
            self.direcionado = True

        g = Grafo(self.n, self.direcionado)

        ## Adiciona as arestas
        for i in self.lista_final:
            g.adiciona_aresta(i[0], i[1], i[2])

        ## A matriz é retornada e armazenada em matriz_str
        matriz_str = g.mostra_matriz()

        ## Ajuste gráfico
        tam_fonte = 5
        if self.n < 15:
            tam_fonte = 20
        else:
            tam_fonte = 15

        font = QtGui.QFont("Arial", tam_fonte)
        self.label.setFont(font)

        ## Imprime na tela a matrizØ
        self.label.setText(matriz_str)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
