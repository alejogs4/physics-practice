from math import sqrt
# class to calculate speed and save data in csv
class physics():
    def calculate_speed(self, inputs, label):
        speed = sqrt( (2 * 9.8*(float(inputs[0].get()) - float(inputs[1].get()))) / float(inputs[2].get()) )
        label.config(text ="La velocidad es " + str(speed))

    def calculate_speed_and_save_results(self):
        return 2