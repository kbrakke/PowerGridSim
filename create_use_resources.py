
class Resource():

    def __init__(self, total_supply, start_allocation, capacity_list):
        self.total_supply = total_supply
        self.start_allocation = start_allocation
        self.capacity_list = capacity_list

    def initialize_supply(self):
        """place the initial supply of the resource at the start of the game into the capacity_list"""
        unit_count = 0
        for i in range(self.start_allocation[0 ] -1, self.start_allocation[1]):
            for j in range(len(self.capacity_list[i][1])):
                self.capacity_list[i][1][j] = 1
                unit_count += 1
        self.total_supply -= unit_count

    def poss_purchases(self):
        poss_pur_dict = {}
        bin_count = 1
        bin_cost = 0
        for bin in self.capacity_list:
            for res in bin[1]:
                if res == 1:
                    poss_pur_dict[bin_count] = bin_cost  + bin[0]
                    bin_count += 1
                    bin_cost += bin[0]
        return poss_pur_dict


    def buy_resource(self, num_res):
        """checks the purchase and reduces the supply on the board returns tuple of number of units and total cost"""
        check_pur = self.poss_purchases()
        if num_res in check_pur.keys():
            update_res = num_res
            for bin in self.capacity_list:
                for i, res in enumerate(bin[1]):
                    if res == 1 and update_res > 0:
                        bin[1][i] = 0
                        update_res -= 1
            return (num_res, check_pur[num_res])
        else:
            return 'not enough resources'



    def use_resource(self, num_units):
        '''put the used resource back in inventory'''
        self.total_supply += num_units



    def resupply(self, resupply_units):
        '''resupply the resource at the end of the turn update capacity list'''
        units_place = max(resupply_units, self.total_supply)
        for i in range(len(self.capacity_list)-1, 0, -1):
            for j in range(len(self.capacity_list[i][1])-1, -1, -1):
                if self.capacity_list[i][1][j] == 0 and units_place > 0:
                    self.capacity_list[i][1][j] = 1
                    units_place -= 1



    def show_board(self):
        """print list of resource currently on the board"""
        print(self.capacity_list)

    def show_supply(self):
        """print list of resource currently on the board"""
        print(self.total_supply)


total_supply_coal = 27
start_supply_coal = (2, 9)
# total_supply_gas = 24
# start_supply_gas = (3, 8)
# total_supply_oil = 20
# start_supply_oil = (3, 9)
# total_supply_uranium = 12
# start_supply_uranium = (8, 9)




coal_cl = [[1 ,[0 ,0 ,0 ,0]] ,[2 ,[0 ,0 ,0 ,0]] ,[3 ,[0 ,0 ,0 ,0]] ,[4 ,[0 ,0 ,0 ,0]] ,[5 ,[0 ,0 ,0 ,0]]
           ,[6, [0 ,0 ,0 ,0]] ,[7, [0 ,0]] ,[8, [0 ,0]] ,[9, [0 ,0]]]
gas_cl = [[1, [0, 0, 0, 0]], [2, [0, 0, 0, 0]], [3, [0, 0, 0, 0]], [4, [0, 0, 0, 0]], [5, [0, 0, 0, 0]]
    , [6, [0, 0, 0, 0]], [7, [0, 0]], [8, [0, 0]], [9, [0, 0]]]
oil_cl = [[1, [0, 0, 0, 0]], [2, [0, 0, 0, 0]], [3, [0, 0, 0, 0]], [4, [0, 0, 0, 0]], [5, [0, 0, 0, 0]]
    , [6, [0, 0, 0, 0]], [7, [0, 0]], [8, [0, 0]], [9, [0, 0]]]
uranium_cl = [[1, [0, 0, 0, 0]], [2, [0, 0, 0, 0]], [3, [0, 0, 0, 0]], [4, [0, 0, 0, 0]], [5, [0, 0, 0, 0]]
    , [6, [0, 0, 0, 0]], [7, [0, 0]], [8, [0, 0]], [9, [0, 0]]]

coal = Resource(total_supply_coal, start_supply_coal, coal_cl)
coal.initialize_supply()
# gas = Resource(total_supply_gas, start_supply_gas, gas_cl)
# gas.initialize_supply()
# oil = Resource(total_supply_oil, start_supply_oil, oil_cl)
# oil.initialize_supply()
# uranium = Resource(total_supply_uranium, start_supply_uranium, uranium_cl)
# uranium.initialize_supply()

print('total resource supply')
coal.show_supply()
print('starting resource board')
coal.show_board()
coal.show_supply()
print('purchase resource')
print(coal.poss_purchases())
print(coal.buy_resource(12))
# oil.show_board()
# gas.show_board()
# uranium.show_board()
print('board after purchase')
coal.show_board()
print('use resource')
coal.use_resource(2)
coal.show_supply()
print('resupply after turn add 5')
coal.resupply(5)
coal.show_board()
