from PyQt5 import QtWidgets, QtCore
from _studentBox import Ui_StudentBox

from student import Student


class StudentBox(object):
    """学生信息编辑盒 - 基类"""

    def __init__(self):

        self.dialog = QtWidgets.QDialog()
        window = Ui_StudentBox()
        window.setupUi(self.dialog)

        self.indexEdit = window.indexEdit
        self.nameEdit = window.nameEdit
        self.birthEdit = window.birthEdit
        self.majorEdit = window.majorEdit
        self.gradeEdit = window.gradeEdit
        self.classEdit = window.classEdit

        self.okButton = window.okButton
        self.cancelButton = window.cancelButton

        self.msgLabel = window.msg

        self.okButton.clicked.connect(self.onFinished)

    def show(self):
        self.dialog.show()

    def setTitle(self, title):
        self.dialog.setWindowTitle(title)

    def setMsg(self, text):
        self.msgLabel.setText(text)

    def setButton(self, ok, cancel=None):
        self.okButton.setText(ok)
        self.cancelButton.setText(cancel) if cancel is not None else None

    def applyToStudent(self, student):
        student.index = self.indexEdit.text()
        student.name = self.nameEdit.text()
        student.birth = self.birthEdit.text()
        student.major = self.majorEdit.text()
        student.grade = self.gradeEdit.text()
        student.classname = self.classEdit.text()

    def onFinished(self):
        pass


class EditBox(StudentBox):
    """编辑学生信息 - 继承StudentBox"""

    def __init__(self, student, callback):
        super(EditBox, self).__init__()
        self.student = student
        self.callback = callback

        self.setTitle("修改信息...")
        self.setMsg("")
        self.setButton("修改")

        self.indexEdit.setText(student.index)
        self.nameEdit.setText(student.name)
        self.birthEdit.setText(student.birth)
        self.majorEdit.setText(student.major)
        self.gradeEdit.setText(student.grade)
        self.classEdit.setText(student.classname)

    def onFinished(self):
        student = self.student
        self.applyToStudent(student)
        self.callback(student)


class NewBox(StudentBox):
    """新建学生档案 - 继承StudentBox"""

    def __init__(self, callback):
        super(NewBox, self).__init__()
        self.callback = callback

        self.setTitle("新建档案...")
        self.setMsg("")
        self.setButton("新建")

        self.student = Student()

    def onFinished(self):
        student = self.student
        self.applyToStudent(student)
        self.callback(self.student)


class SearchBox(StudentBox):
    """高级搜索框 - 继承StudentBox"""

    def __init__(self, callback):
        super(SearchBox, self).__init__()
        self.callback = callback

        self.setTitle("高级搜索...")
        self.setMsg("请输入关键词, 多个条件用空格分隔")
        self.setButton("搜索")

    def onFinished(self):
        keyList = [
            ("index", ' '.join(self.indexEdit.text().split())),
            ("name", ' '.join(self.nameEdit.text().split())),
            ("birth", ' '.join(self.birthEdit.text().split())),
            ("major", ' '.join(self.majorEdit.text().split())),
            ("grade", ' '.join(self.gradeEdit.text().split())),
            ("classname", ' '.join(self.classEdit.text().split()))
        ]
        self.callback(keyList)
