from PyQt5 import QtCore, QtGui, QtWidgets


class WizardUI(object):
    def setup_ui(self, wizard):
        wizard.setObjectName("wizard")
        wizard.resize(732, 425)
        wizard.setMinimumSize(QtCore.QSize(575, 400))
        wizard.setWindowTitle("Digital Collection Annotation Assistant")
        wizard.setOptions(QtWidgets.QWizard.NoBackButtonOnStartPage | QtWidgets.QWizard.NoCancelButton)
        wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)

        # page 1 contents
        self.wizardpage1 = QtWidgets.QWizardPage()
        self.wizardpage1.setObjectName("wizardpage1")
        self.gridlayout_wp1_0 = QtWidgets.QGridLayout(self.wizardpage1)
        self.gridlayout_wp1_0.setObjectName("gridlayout_wp1")

        self.scrollarea = QtWidgets.QScrollArea(self.wizardpage1)
        self.scrollarea.setMinimumSize(QtCore.QSize(400, 0))
        self.scrollarea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setObjectName("scrollarea")
        self.scrollarea_widget = QtWidgets.QWidget()
        self.scrollarea_widget.setGeometry(QtCore.QRect(0, 0, 684, 374))
        self.scrollarea_widget.setObjectName("scrollarea_widget")
        self.gridlayout_wp1_1 = QtWidgets.QGridLayout(self.scrollarea_widget)
        self.gridlayout_wp1_1.setObjectName("gridlayout")
        self.verticallayout_wp1_0 = QtWidgets.QVBoxLayout()
        self.verticallayout_wp1_0.setObjectName("verticallayout")

        self.consentbox = QtWidgets.QCheckBox(self.scrollarea_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.consentbox.sizePolicy().hasHeightForWidth())
        self.consentbox.setSizePolicy(sizePolicy)
        self.consentbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.consentbox.setObjectName("consentbox")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.welcomelabel = QtWidgets.QLabel(self.scrollarea_widget)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setWordWrap(True)
        self.welcomelabel.setOpenExternalLinks(True)
        self.welcomelabel.setObjectName("welcomelabel")
        self.reblabel = QtWidgets.QLabel(self.scrollarea_widget)
        self.reblabel.setFont(font)
        self.reblabel.setWordWrap(True)
        self.reblabel.setOpenExternalLinks(True)
        self.reblabel.setObjectName("reblabel")
        self.consent_savebutton = QtWidgets.QPushButton(self.scrollarea_widget)
        self.consent_savebutton.setObjectName("consent_savebutton")

        self.verticallayout_wp1_0.addWidget(self.welcomelabel)
        self.verticallayout_wp1_0.addWidget(self.consentbox)
        self.verticallayout_wp1_0.addWidget(self.reblabel)
        self.verticallayout_wp1_0.addWidget(
            self.consent_savebutton, 0, QtCore.Qt.AlignHCenter)
        self.gridlayout_wp1_1.addLayout(self.verticallayout_wp1_0, 1, 0, 1, 1)
        self.scrollarea.setWidget(self.scrollarea_widget)
        self.gridlayout_wp1_0.addWidget(self.scrollarea, 0, 0, 1, 1)

        # page 2 contents
        self.wizardpage2 = QtWidgets.QWizardPage()
        self.wizardpage2.setObjectName("wizardpage2")
        self.verticallayout_wp2_0 = QtWidgets.QVBoxLayout(self.wizardpage2)
        self.verticallayout_wp2_0.setObjectName("verticallayout_wp2_0")
        self.horizontallayout_wp2_0 = QtWidgets.QHBoxLayout()
        self.horizontallayout_wp2_0.setObjectName("horizontallayout_wp2_0")

        self.og_tree_key = QtWidgets.QTreeView()
        self.og_tree_0 = QtWidgets.QTreeView()
        self.reset_demo_btn = QtWidgets.QPushButton()
        self.reset_demo_btn.resize(self.reset_demo_btn.sizeHint())
        self.horizontallayout_wp2_0.addStretch(1)
        self.horizontallayout_wp2_0.addWidget(self.reset_demo_btn)
        self.horizontallayout_wp2_0.addStretch(1)
        self.verticallayout_wp2_0.addWidget(self.og_tree_key)
        self.verticallayout_wp2_0.addWidget(self.og_tree_0)
        self.verticallayout_wp2_0.addLayout(self.horizontallayout_wp2_0)

        # page 3 contents
        self.wizardpage3 = QtWidgets.QWizardPage()
        self.wizardpage3.setObjectName("wizardpage3")
        self.verticallayout_wp3_0 = QtWidgets.QVBoxLayout(self.wizardpage3)
        self.verticallayout_wp3_0.setObjectName("verticallayout_wp3_0")
        self.horizontallayout_wp3_0 = QtWidgets.QHBoxLayout()
        self.horizontallayout_wp3_0.setObjectName("horizontallayout_wp3_0")

        self.textarea_wp3_0 = QtWidgets.QPlainTextEdit()
        self.verticallayout_wp3_0.addWidget(self.textarea_wp3_0)
        self.verticallayout_wp3_0.addLayout(self.horizontallayout_wp3_0)

        # page 4 contents
        self.wizardpage4 = QtWidgets.QWizardPage()
        self.wizardpage4.setObjectName("wizardpage4")
        self.verticallayout_wp4_0 = QtWidgets.QVBoxLayout(self.wizardpage4)
        self.verticallayout_wp4_0.setObjectName("verticallayout_wp4_0")
        self.horizontallayout_wp4_0 = QtWidgets.QHBoxLayout()
        self.horizontallayout_wp4_0.setObjectName("horizontallayout_wp4_0")

        self.og_tree_1 = QtWidgets.QTreeView()
        self.select_btn_1 = QtWidgets.QPushButton()
        self.select_btn_1.resize(self.select_btn_1.sizeHint())
        self.save_btn_1 = QtWidgets.QPushButton()
        self.save_btn_1.resize(self.save_btn_1.sizeHint())
        self.save_btn_1.setDisabled(True)
        self.load_btn_1 = QtWidgets.QPushButton()
        self.load_btn_1.resize(self.load_btn_1.sizeHint())
        self.less_btn_1 = QtWidgets.QPushButton()
        self.less_btn_1.resize(self.less_btn_1.sizeHint())
        self.less_btn_1.setDisabled(True)
        self.horizontallayout_wp4_0.addStretch(1)
        self.horizontallayout_wp4_0.addWidget(self.select_btn_1)
        self.horizontallayout_wp4_0.addWidget(self.save_btn_1)
        self.horizontallayout_wp4_0.addWidget(self.load_btn_1)
        self.horizontallayout_wp4_0.addWidget(self.less_btn_1)
        self.horizontallayout_wp4_0.addStretch(1)
        self.verticallayout_wp4_0.addWidget(self.og_tree_1)
        self.verticallayout_wp4_0.addLayout(self.horizontallayout_wp4_0)

        # page 5 contents
        self.wizardpage5 = QtWidgets.QWizardPage()
        self.wizardpage5.setObjectName("wizardpage5")
        self.gridlayout_wp5_0 = QtWidgets.QGridLayout(self.wizardpage4)
        self.gridlayout_wp5_0.setObjectName("gridlayout_wp5")

        # all pages
        self.retranslate_ui(wizard)
        wizard.addPage(self.wizardpage1)
        wizard.addPage(self.wizardpage2)
        wizard.addPage(self.wizardpage4) #show annotations task (4) after training (2)
        wizard.addPage(self.wizardpage3) #ask about software (3) after annotation task
        wizard.addPage(self.wizardpage5)

    def retranslate_ui(self, wizard):
        _translate = QtCore.QCoreApplication.translate
        # page 1 labels
        self.wizardpage1.setTitle(_translate("Wizard", "Introduction"))
        self.wizardpage1.setSubTitle(_translate(
            "Wizard",
            "Please read the information below, click the check box to consent and participate, and click \'Next\' to begin."))
        self.welcomelabel.setText(_translate(
            "Wizard",
            "<html><head/><body><p align=\"justify\"><span style=\" "
            #"font-weight:600;\">WARNING</span></p>
            "<p align=\"justify\">"
            #"DEBUG BUILD ONLY. SHOULD  NOT BE RUN BY END USER. Lorem ipsum "
            #"-- populate with consent form, contact information, research "
            #"ethics approval, etc. <span style=\" font-weight:600;\">"
            #"...text...</span><span style=\" font-weight:600; "
            #"font-style:italic;\">.</span> ...text... <span style=\" "
            #"font-style:italic;\">...text...</span>."
            "Welcome! Thank you for participating in our study, which aims to test a tool for anotating your collection such that it could be interpreted by someone else in the future, for example by a curator if you were to donate it to a museum, or by a family member if you were to pass on your collection. In what follows you will be trained in using the tool on a small demonstration collection, and then will annotate your own collection on this computer. Afterwards the researcher will ask you a few questions about your use and perceptions of the tool. You may ask them questions at any time."
            "</p></body></html>"))
        self.consentbox.setText(_translate(
            "Wizard", "I understand and consent to participate: "))
        self.reblabel.setText(_translate(
            "Wizard",
            "<html><head/><body><p align=\"justify\">This software is provided as a part of the <a href=\"http://hiddenheritage.vuw.ac.nz\"><span style=\" "
            "text-decoration: underline; color:#2980b9;\">Hidden Heritage</span></a> research project run by Drs Maja Krtalić and Jesse Dinneen, with Profs Chern Li Liew and Anne Goulding, at Victoria University of Wellington, and was approved by the university's Human Ethics Committee (HEC #27173). If you have any questions about your participation in this study, please contact <a href=\"mailto:jesse.dinneen@vuw.ac.nz\"><span style=\" "
            "text-decoration: underline; color:#2980b9;\">Dr Dinneen</span></a>, and if you have any questions or concerns regarding your rights or welfare as a participant in this study, please contact the Human Ethics Committee</a> via <a href=\"mailto:hec@vuw.ac.nz\"><span style=\" "
            "text-decoration: underline; color:#2980b9;\">email</span></a> or telephone (+64-4-463-6028).</p></body></html>"))
        self.consent_savebutton.setText(_translate(
            "Wizard", "Save this info to file (optional)"))
        # page 2 labels
        self.wizardpage2.setTitle(_translate("Wizard", "Training"))
        self.wizardpage2.setSubTitle(_translate(
            "Wizard",
            "This screen provides training on using the annotation tool. Please listen to the researcher's explanation of how to use the tool, try it for your self, and once you feel comfortable using it, press \'Next\' to continue."))
        self.reset_demo_btn.setText(_translate("Wizard", "Reset"))
        self.reset_demo_btn.setToolTip(_translate(
            "Wizard", "Return example folder structure to initial state."))

        # page 3 labels
        self.wizardpage3.setTitle(_translate("Wizard", "Listing uncommon software"))
        self.wizardpage3.setSubTitle(_translate(
            "Wizard",
            "Please list any software needed to view your collection if someone outside your field or family is unlikely to know it, for example: \"LaTeX for <span style=\" "
            "font-style:italic;\">.tex</span> files\". You can omit very common software like Microsoft Word."))

        # page 4 labels
        self.wizardpage4.setTitle(_translate("Wizard", "Annotate your collection"))
        self.wizardpage4.setSubTitle(_translate(
            "Wizard",
            "Please indicate which parts of your collection are relevant (or should be excluded/ignored). Load your collection with \'Find folders\', and when finished annotating, \'Save\' your work and click \'Next\' to continue."))
        self.select_btn_1.setText(_translate("Wizard", "Find folders"))
        self.select_btn_1.setToolTip(_translate(
            "Wizard", "Select <b>personal folder</b> for data collection."))
        self.save_btn_1.setText(_translate("Wizard", "Save"))
        self.save_btn_1.setToolTip(_translate(
            "Wizard",
            "Save folder structure data and software choices locally as a "
            "JSON file."))
        self.load_btn_1.setText(_translate("Wizard", "Load"))
        self.load_btn_1.setToolTip(_translate(
            "Wizard",
            "Load folder structure data and software choices from a "
            "JSON file."))
        self.less_btn_1.setText(_translate("Wizard", "Show less"))
        self.less_btn_1.setToolTip(_translate(
            "Wizard",
            "Collapses all folders except the root."))

        # page 5 labels
        self.wizardpage5.setTitle(_translate("Wizard", "Finished!"))
        self.wizardpage5.setSubTitle(_translate(
            "Wizard",
            "Thank you -- please refer to the researcher for instructions on completing participation."))
