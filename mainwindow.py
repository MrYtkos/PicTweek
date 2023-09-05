import sys
import cv2
import numpy as np

from PySide6.QtGui import QPixmap, Qt, QImage
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QMessageBox
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.graphicsView.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)

        self.ui.applyButton.hide()
        self.ui.cancelButton.hide()

        self.current_image = None
        self.modified_image = None
        self.inwrite_image = None
        self.update_image = None

        self.ui.filterBox.currentIndexChanged.connect(self.apply_filter)
        self.ui.chooseButton.clicked.connect(self.choosefile)
        self.ui.changeButton.clicked.connect(self.changefile)
        self.ui.saveButton.clicked.connect(self.save_image)
        self.ui.saveasButton.clicked.connect(self.save_as_image)
        self.ui.filterSlider.valueChanged.connect(self.apply_filter)


        self.ui.label_4.hide()
        self.ui.filterLabel.hide()
        self.ui.filterSlider.hide()
        self.ui.filterLabel.setText("1")

        self.ui.filterSlider.setMinimum(1)
        self.ui.filterSlider.setMaximum(99)
        self.ui.filterSlider.setValue(1)
        self.ui.filterSlider.setTickInterval(2)
        self.ui.filterSlider.setSingleStep(2)
        self.ui.filterSlider.valueChanged.connect(self.on_filter_slider_value_changed)
        self.ui.filterSlider.valueChanged.connect(self.apply_filter)


        self.ui.brightnessSlider.setEnabled(0)
        self.ui.brightnessSlider.setMinimum(-100)
        self.ui.brightnessSlider.setMaximum(100)
        self.ui.brightnessSlider.setValue(0)
        self.ui.brightnessSlider.valueChanged.connect(lambda:self.on_slider_value_changed(value = self.ui.brightnessSlider.value(),wht = 1))
        self.ui.brightnessSlider.valueChanged.connect(self.apply_filter)

        self.ui.changeButton.hide()

        self.ui.contrastSlider.setEnabled(0)
        self.ui.contrastSlider.setMinimum(-100)
        self.ui.contrastSlider.setMaximum(100)
        self.ui.contrastSlider.setValue(0)
        self.ui.contrastSlider.valueChanged.connect(lambda:self.on_slider_value_changed(value = self.ui.contrastSlider.value(), wht = 2))
        self.ui.contrastSlider.valueChanged.connect(self.apply_filter)

        self.ui.applyButton.clicked.connect(self.apply_changes)
        self.ui.cancelButton.clicked.connect(self.cancel_changes)

        self.ui.filterBox.setEnabled(0)

        self.ui.brightnessLabel.hide()
        self.ui.brightnessSlider.hide()

        self.ui.contrastLabel.hide()
        self.ui.contrastSlider.hide()

        self.ui.label_2.hide()
        self.ui.label_3.hide()



    def on_slider_value_changed(self, value, wht):
        if wht == 1:
            self.ui.brightnessLabel.setText(str(value))
        if wht == 2:
            self.ui.contrastLabel.setText(str(value))
        if wht == 3:
            self.ui.filterLabel.setText(str(value))

    def on_filter_slider_value_changed(self, value):
    # Проверка, является ли новое значение четным числом
        if value % 2 == 0:
            # Увеличение значения на 1, если оно четное
            self.ui.filterSlider.setValue(value + 1)
            self.ui.filterSlider.valueChanged.connect(lambda:self.on_slider_value_changed(value = self.ui.filterSlider.value(),wht = 3))


    def choosefile(self):
        global file_path
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', 'Images (*.png *.jpg *.jpeg)')
        if file_path:
            print(f"Выбран файл: {file_path}")
            self.current_image = cv2.imread(file_path)

            pixmap = QPixmap.fromImage(QImage(self.current_image.data, self.current_image.shape[1], self.current_image.shape[0], QImage.Format_BGR888))
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.scene.setSceneRect(0, 0, self.current_image.shape[1], self.current_image.shape[0])
            self.ui.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

            self.ui.chooseButton.hide()
            self.ui.changeButton.show()


            self.ui.filterBox.setEnabled(1)

            self.modified_image = self.current_image.copy()

    def changefile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', 'Images (*.png *.jpg *.jpeg)')
        if file_path:
            print(f"Выбран файл: {file_path}")
            self.current_image = cv2.imread(file_path)

            pixmap = QPixmap.fromImage(QImage(self.current_image.data, self.current_image.shape[1], self.current_image.shape[0], QImage.Format_BGR888))
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.scene.setSceneRect(0, 0, self.current_image.shape[1], self.current_image.shape[0])
            self.ui.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

            self.modified_image = self.current_image.copy()

            self.ui.brightnessSlider.setValue(0)
            self.ui.contrastSlider.setValue(0)


    def apply_filter(self):
        if self.current_image is not None:
            image = self.modified_image
            selected_filter = self.ui.filterBox.currentText()
            filter_strength = int(self.ui.filterLabel.text())
            brightnessvalue = int(self.ui.brightnessLabel.text())
            contrastvalue =  int(self.ui.contrastLabel.text())

            if selected_filter == 'Без фильтров':
                self.ui.filterSlider.setValue(1)

                self.ui.applyButton.hide()
                self.ui.cancelButton.hide()

                self.ui.label_4.hide()
                self.ui.filterLabel.hide()
                self.ui.filterSlider.hide()

                self.ui.label_2.hide()
                self.ui.contrastLabel.hide()
                self.ui.contrastSlider.hide()

                self.ui.label_3.hide()
                self.ui.brightnessLabel.hide()
                self.ui.brightnessSlider.hide()

                self.update_image = self.modified_image.copy()
                self.display_image(image)

            if selected_filter == 'Размытие':
                self.ui.label_2.hide()
                self.ui.label_3.hide()
                self.ui.brightnessLabel.hide()
                self.ui.brightnessSlider.hide()
                self.ui.contrastLabel.hide()
                self.ui.contrastSlider.hide()

                self.ui.applyButton.show()
                self.ui.cancelButton.show()

                self.ui.label_4.show()
                self.ui.label_4.setText("Степень размытия:")
                self.ui.filterSlider.show()
                self.update_image = cv2.GaussianBlur(image, (filter_strength, filter_strength), 0)
                self.display_image(self.update_image)

            if selected_filter == 'Яркость':
                self.ui.label_4.hide()
                self.ui.filterLabel.hide()
                self.ui.filterSlider.hide()

                self.ui.applyButton.show()
                self.ui.cancelButton.show()

                self.ui.label_2.show()
                self.ui.label_3.show()
                self.ui.brightnessLabel.show()
                self.ui.brightnessSlider.show()
                self.ui.contrastLabel.show()
                self.ui.contrastSlider.show()

                self.ui.brightnessSlider.setEnabled(1)
                self.ui.contrastSlider.setEnabled(1)

                self.update_image = cv2.convertScaleAbs(image, alpha = 1.0 + (brightnessvalue / 100.0), beta= 1.0 + contrastvalue )
                self.display_image(self.update_image)

            if selected_filter == 'Чёрно-белый':
                self.ui.label_4.hide()
                self.ui.filterSlider.hide()

                self.ui.applyButton.show()
                self.ui.cancelButton.show()

                self.ui.label_2.hide()
                self.ui.contrastLabel.hide()
                self.ui.contrastSlider.hide()

                self.ui.label_3.hide()
                self.ui.brightnessLabel.hide()
                self.ui.brightnessSlider.hide()

                self.update_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                self.update_image = cv2.cvtColor(self.update_image, cv2.COLOR_GRAY2BGR)
                self.display_image(self.update_image)

            if selected_filter == 'Негатив':
                self.ui.label_4.hide()
                self.ui.filterSlider.hide()

                self.ui.applyButton.show()
                self.ui.cancelButton.show()

                self.ui.label_2.hide()
                self.ui.contrastLabel.hide()
                self.ui.contrastSlider.hide()

                self.ui.label_3.hide()
                self.ui.brightnessLabel.hide()
                self.ui.brightnessSlider.hide()

                self.update_image = 255 - image
                self.display_image(self.update_image)

            if selected_filter == 'Увеличение резкости':
                self.ui.applyButton.show()
                self.ui.cancelButton.show()

                self.ui.label_2.hide()
                self.ui.contrastLabel.hide()
                self.ui.contrastSlider.hide()

                self.ui.label_3.hide()
                self.ui.brightnessLabel.hide()
                self.ui.brightnessSlider.hide()

                self.ui.label_4.hide()
                self.ui.filterSlider.hide()

                sharpen_kernel = np.array([
                    [-1, -1, -1],
                    [-1,  9, -1],
                    [-1, -1, -1]
                ])

                self.update_image = cv2.filter2D(image, -1, sharpen_kernel)
                self.display_image(self.update_image)

            if selected_filter == 'Границы обьектов':
                self.ui.applyButton.show()
                self.ui.cancelButton.show()

                self.ui.label_2.hide()
                self.ui.contrastLabel.hide()
                self.ui.contrastSlider.hide()

                self.ui.label_3.hide()
                self.ui.brightnessLabel.hide()
                self.ui.brightnessSlider.hide()

                self.ui.label_4.hide()
                self.ui.filterSlider.hide()

                self.update_image = cv2.Sobel(image, ddepth=-1, dx=1, dy=1, ksize=5)
                self.display_image(self.update_image)

    def apply_changes(self):
        self.modified_image = self.update_image.copy()
        self.inwrite_image = self.update_image.copy()

        self.ui.brightnessSlider.setValue(0)
        self.ui.contrastSlider.setValue(0)
        self.ui.filterSlider.setValue(1)
        self.ui.applyButton.hide()
        self.ui.cancelButton.hide()
        print("done")

    def cancel_changes(self):
        self.update_image = self.modified_image.copy()
        self.ui.brightnessSlider.setValue(0)
        self.ui.contrastSlider.setValue(0)
        self.ui.filterSlider.setValue(0)
        print("done")

    def display_image(self, image):
            pixmap = QPixmap.fromImage(QImage(image.data, image.shape[1], image.shape[0], QImage.Format_BGR888))
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.ui.graphicsView.resetTransform()
            self.ui.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)


    def save_image(self):
        cv2.imwrite(str(file_path), self.inwrite_image)
        print(str(file_path))

    def save_as_image(self):
        if self.update_image is None:
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "PNG Image (*.png);;JPEG Image (*.jpg *.jpeg)")
        if file_path:
            cv2.imwrite(file_path, self.inwrite_image)
            print(f"Файл сохранен: {file_path}")

    def closeEvent(self, event):
            if self.update_image is not None:
                reply = QMessageBox.question(self, 'Сохранить изображение', 'Хотите сохранить изменения?',
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                if reply == QMessageBox.Yes:
                    self.save_as_image()
                elif reply == QMessageBox.Cancel:
                    event.ignore()
                    return
            super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
