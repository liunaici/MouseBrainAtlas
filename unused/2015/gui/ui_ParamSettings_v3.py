# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'param_settings_v2.ui'
#
# Created: Fri Jan 30 17:18:15 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ParameterSettingsWindow(object):
    def setupUi(self, ParameterSettingsWindow):
        ParameterSettingsWindow.setObjectName(_fromUtf8("ParameterSettingsWindow"))
        ParameterSettingsWindow.resize(975, 831)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        ParameterSettingsWindow.setFont(font)
        self.verticalLayout = QtGui.QVBoxLayout(ParameterSettingsWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gaborFrame = QtGui.QFrame(ParameterSettingsWindow)
        self.gaborFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gaborFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.gaborFrame.setObjectName(_fromUtf8("gaborFrame"))
        self.horizontalLayout_24 = QtGui.QHBoxLayout(self.gaborFrame)
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.gaborListLayout = QtGui.QVBoxLayout()
        self.gaborListLayout.setObjectName(_fromUtf8("gaborListLayout"))
        self.label = QtGui.QLabel(self.gaborFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.gaborListLayout.addWidget(self.label)
        self.list_gabor = QtGui.QListWidget(self.gaborFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_gabor.sizePolicy().hasHeightForWidth())
        self.list_gabor.setSizePolicy(sizePolicy)
        self.list_gabor.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.list_gabor.setFrameShape(QtGui.QFrame.WinPanel)
        self.list_gabor.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.list_gabor.setProperty("showDropIndicator", False)
        self.list_gabor.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.list_gabor.setObjectName(_fromUtf8("list_gabor"))
        item = QtGui.QListWidgetItem()
        self.list_gabor.addItem(item)
        self.gaborListLayout.addWidget(self.list_gabor)
        self.horizontalLayout_24.addLayout(self.gaborListLayout)
        self.formFrame = QtGui.QFrame(self.gaborFrame)
        self.formFrame.setObjectName(_fromUtf8("formFrame"))
        self.formLayout = QtGui.QFormLayout(self.formFrame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formFrame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinBox_min_wavelen = QtGui.QSpinBox(self.formFrame)
        self.spinBox_min_wavelen.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_min_wavelen.setMaximum(9999)
        self.spinBox_min_wavelen.setObjectName(_fromUtf8("spinBox_min_wavelen"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinBox_min_wavelen)
        self.label_3 = QtGui.QLabel(self.formFrame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formFrame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtGui.QLabel(self.formFrame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_5 = QtGui.QLabel(self.formFrame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.spinBox_max_wavelen = QtGui.QSpinBox(self.formFrame)
        self.spinBox_max_wavelen.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_max_wavelen.setMaximum(9999)
        self.spinBox_max_wavelen.setObjectName(_fromUtf8("spinBox_max_wavelen"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBox_max_wavelen)
        self.spinBox_freq_step = QtGui.QSpinBox(self.formFrame)
        self.spinBox_freq_step.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_freq_step.setMaximum(9999)
        self.spinBox_freq_step.setObjectName(_fromUtf8("spinBox_freq_step"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_freq_step)
        self.spinBox_bandwidth = QtGui.QDoubleSpinBox(self.formFrame)
        self.spinBox_bandwidth.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_bandwidth.setMaximum(9999.99)
        self.spinBox_bandwidth.setObjectName(_fromUtf8("spinBox_bandwidth"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBox_bandwidth)
        self.spinBox_theta_interval = QtGui.QSpinBox(self.formFrame)
        self.spinBox_theta_interval.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_theta_interval.setMaximum(9999)
        self.spinBox_theta_interval.setObjectName(_fromUtf8("spinBox_theta_interval"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinBox_theta_interval)
        self.horizontalLayout_24.addWidget(self.formFrame)
        self.verticalLayout.addWidget(self.gaborFrame)
        self.segmFrame = QtGui.QFrame(ParameterSettingsWindow)
        self.segmFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.segmFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.segmFrame.setObjectName(_fromUtf8("segmFrame"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.segmFrame)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.segListLayout = QtGui.QVBoxLayout()
        self.segListLayout.setObjectName(_fromUtf8("segListLayout"))
        self.label_14 = QtGui.QLabel(self.segmFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.segListLayout.addWidget(self.label_14)
        self.segm_list = QtGui.QListWidget(self.segmFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.segm_list.sizePolicy().hasHeightForWidth())
        self.segm_list.setSizePolicy(sizePolicy)
        self.segm_list.setFrameShape(QtGui.QFrame.WinPanel)
        self.segm_list.setEditTriggers(QtGui.QAbstractItemView.EditKeyPressed)
        self.segm_list.setProperty("showDropIndicator", False)
        self.segm_list.setObjectName(_fromUtf8("segm_list"))
        self.segListLayout.addWidget(self.segm_list)
        self.horizontalLayout_21.addLayout(self.segListLayout)
        self.frame_4 = QtGui.QFrame(self.segmFrame)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setLineWidth(28)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.formLayout_2 = QtGui.QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_7 = QtGui.QLabel(self.frame_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.spinBox_n_superpixels = QtGui.QSpinBox(self.frame_4)
        self.spinBox_n_superpixels.setMaximumSize(QtCore.QSize(55, 27))
        self.spinBox_n_superpixels.setMaximum(9999)
        self.spinBox_n_superpixels.setObjectName(_fromUtf8("spinBox_n_superpixels"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinBox_n_superpixels)
        self.label_8 = QtGui.QLabel(self.frame_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.spinBox_slic_compactness = QtGui.QSpinBox(self.frame_4)
        self.spinBox_slic_compactness.setMaximumSize(QtCore.QSize(55, 27))
        self.spinBox_slic_compactness.setMaximum(9999)
        self.spinBox_slic_compactness.setObjectName(_fromUtf8("spinBox_slic_compactness"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBox_slic_compactness)
        self.label_9 = QtGui.QLabel(self.frame_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.spinBox_slic_sigma = QtGui.QSpinBox(self.frame_4)
        self.spinBox_slic_sigma.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_slic_sigma.setMaximum(9999)
        self.spinBox_slic_sigma.setObjectName(_fromUtf8("spinBox_slic_sigma"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_slic_sigma)
        self.horizontalLayout_21.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.segmFrame)
        self.vqFrame = QtGui.QFrame(ParameterSettingsWindow)
        self.vqFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vqFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.vqFrame.setObjectName(_fromUtf8("vqFrame"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.vqFrame)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_21 = QtGui.QLabel(self.vqFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_8.addWidget(self.label_21)
        self.list_vq = QtGui.QListWidget(self.vqFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_vq.sizePolicy().hasHeightForWidth())
        self.list_vq.setSizePolicy(sizePolicy)
        self.list_vq.setFrameShape(QtGui.QFrame.WinPanel)
        self.list_vq.setProperty("showDropIndicator", False)
        self.list_vq.setObjectName(_fromUtf8("list_vq"))
        self.verticalLayout_8.addWidget(self.list_vq)
        self.horizontalLayout_20.addLayout(self.verticalLayout_8)
        self.frame_6 = QtGui.QFrame(self.vqFrame)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setLineWidth(28)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.formLayout_3 = QtGui.QFormLayout(self.frame_6)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_15 = QtGui.QLabel(self.frame_6)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_15)
        self.spinBox_n_texton = QtGui.QSpinBox(self.frame_6)
        self.spinBox_n_texton.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_n_texton.setMaximum(9999)
        self.spinBox_n_texton.setObjectName(_fromUtf8("spinBox_n_texton"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinBox_n_texton)
        self.label_16 = QtGui.QLabel(self.frame_6)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_16)
        self.spinBox_n_sample = QtGui.QSpinBox(self.frame_6)
        self.spinBox_n_sample.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_n_sample.setMaximum(9999)
        self.spinBox_n_sample.setObjectName(_fromUtf8("spinBox_n_sample"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinBox_n_sample)
        self.label_17 = QtGui.QLabel(self.frame_6)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_17)
        self.spinBox_n_iter = QtGui.QSpinBox(self.frame_6)
        self.spinBox_n_iter.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spinBox_n_iter.setMaximum(9999)
        self.spinBox_n_iter.setObjectName(_fromUtf8("spinBox_n_iter"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox_n_iter)
        self.horizontalLayout_20.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.vqFrame)
        self.bottomLayout = QtGui.QFrame(ParameterSettingsWindow)
        self.bottomLayout.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottomLayout.setFrameShadow(QtGui.QFrame.Raised)
        self.bottomLayout.setObjectName(_fromUtf8("bottomLayout"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.bottomLayout)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_11 = QtGui.QLabel(self.bottomLayout)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_14.addWidget(self.label_11)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gaborLabel = QtGui.QLabel(self.bottomLayout)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gaborLabel.setFont(font)
        self.gaborLabel.setObjectName(_fromUtf8("gaborLabel"))
        self.horizontalLayout_2.addWidget(self.gaborLabel)
        self.gaborName = QtGui.QLabel(self.bottomLayout)
        self.gaborName.setObjectName(_fromUtf8("gaborName"))
        self.horizontalLayout_2.addWidget(self.gaborName)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.segmLabel = QtGui.QLabel(self.bottomLayout)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.segmLabel.setFont(font)
        self.segmLabel.setObjectName(_fromUtf8("segmLabel"))
        self.horizontalLayout.addWidget(self.segmLabel)
        self.segmName = QtGui.QLabel(self.bottomLayout)
        self.segmName.setObjectName(_fromUtf8("segmName"))
        self.horizontalLayout.addWidget(self.segmName)
        self.horizontalLayout_14.addLayout(self.horizontalLayout)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.vqLabel = QtGui.QLabel(self.bottomLayout)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.vqLabel.setFont(font)
        self.vqLabel.setObjectName(_fromUtf8("vqLabel"))
        self.horizontalLayout_13.addWidget(self.vqLabel)
        self.vqName = QtGui.QLabel(self.bottomLayout)
        self.vqName.setObjectName(_fromUtf8("vqName"))
        self.horizontalLayout_13.addWidget(self.vqName)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_14)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.bottomLayout)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_25.addWidget(self.okButton)
        self.verticalLayout.addWidget(self.bottomLayout)

        self.retranslateUi(ParameterSettingsWindow)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), ParameterSettingsWindow.close)
        QtCore.QMetaObject.connectSlotsByName(ParameterSettingsWindow)

    def retranslateUi(self, ParameterSettingsWindow):
        ParameterSettingsWindow.setWindowTitle(_translate("ParameterSettingsWindow", "Parameter Set Settings", None))
        self.label.setText(_translate("ParameterSettingsWindow", "gabor", None))
        __sortingEnabled = self.list_gabor.isSortingEnabled()
        self.list_gabor.setSortingEnabled(False)
        item = self.list_gabor.item(0)
        item.setText(_translate("ParameterSettingsWindow", "test", None))
        self.list_gabor.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("ParameterSettingsWindow", "min_wavelen", None))
        self.label_3.setText(_translate("ParameterSettingsWindow", "max_wavelen", None))
        self.label_4.setText(_translate("ParameterSettingsWindow", "freq_step", None))
        self.label_6.setText(_translate("ParameterSettingsWindow", "bandwidth", None))
        self.label_5.setText(_translate("ParameterSettingsWindow", "theta_interval", None))
        self.label_14.setText(_translate("ParameterSettingsWindow", "segmentation", None))
        self.label_7.setText(_translate("ParameterSettingsWindow", "n_superpixels", None))
        self.label_8.setText(_translate("ParameterSettingsWindow", "slic_compactness", None))
        self.label_9.setText(_translate("ParameterSettingsWindow", "slic_sigma", None))
        self.label_21.setText(_translate("ParameterSettingsWindow", "vector quantization", None))
        self.label_15.setText(_translate("ParameterSettingsWindow", "n_texton", None))
        self.label_16.setText(_translate("ParameterSettingsWindow", "n_sample", None))
        self.label_17.setText(_translate("ParameterSettingsWindow", "n_iter", None))
        self.label_11.setText(_translate("ParameterSettingsWindow", "selected parameters:", None))
        self.gaborLabel.setText(_translate("ParameterSettingsWindow", "gabor", None))
        self.gaborName.setText(_translate("ParameterSettingsWindow", "selected_gabor", None))
        self.segmLabel.setText(_translate("ParameterSettingsWindow", "segm", None))
        self.segmName.setText(_translate("ParameterSettingsWindow", "selected_segmentation", None))
        self.vqLabel.setText(_translate("ParameterSettingsWindow", "vq", None))
        self.vqName.setText(_translate("ParameterSettingsWindow", "selected_vector", None))
        self.okButton.setText(_translate("ParameterSettingsWindow", "OK", None))
