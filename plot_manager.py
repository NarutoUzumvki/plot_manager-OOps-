class Candidate :
    def __init__(self ,name ,id):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name + str(self.id)


class Total_Assigned_Plots :
    def __init__(self ):
        self.plot_record = []

    def view_all_assigned(self):
        print(self.plot_record)


class Plot :
    def __init__(self ,plot_no, place ,area ,price):
        self.plot_no = plot_no
        self.place = place
        self.area = area
        self.price = price

    def __str__(self):
        return self.plot_no + self.place + self.area + self.price


class Plot_Assign :
    def __init__(self):
        self.plot_list = []

    def assign_plot(self, candidate ,plot ,total_plots):
        plot_str = (f"Dear {candidate.name} ,Plot No-{plot.plot_no} has been assigned to You...Which is Located in {plot.place} with area {plot.area} sqft. - Whose Price is Rs.{plot.price}.")
        self.plot_list.append(plot_str)
        total_plots.plot_record.append(self.plot_list)

    def show_assigned(self):
        print(self.plot_list)


if __name__ == "__main__" :
    candidate1 = Candidate("Mikey" ,"001")
    candidate2 = Candidate("Kisuke" ,"002")
    candidate3 = Candidate("Saturo" ,"003")
    plot1 = Plot(1 ,"WestBengal" ,45261 ,100000)
    plot2 = Plot(2 ,"Himachal-Pradesh" ,74112 ,560000)
    plot3 = Plot(3 ,"Sikkim" ,45698 ,700000)

    total_assigned = Total_Assigned_Plots()

    assign1 = Plot_Assign()
    assign2 = Plot_Assign()
    assign3 = Plot_Assign()

    assign1.assign_plot(candidate1 ,plot1 ,total_assigned)
    assign2.assign_plot(candidate2 ,plot2 ,total_assigned)
    assign3.assign_plot(candidate3 ,plot3 ,total_assigned)
    assign1.show_assigned()
    assign2.show_assigned()
    assign3.show_assigned()

    print("\nTotal Plots Alloted...\n")

    total_assigned.view_all_assigned()

    

