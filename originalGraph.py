graph_neighbours = {}

#the structure identifies each block as a unique number 
#starting the counter from 0 and going horizontally and skipping X's

def generate_graph():

    add_neighbours('0', ['1', '8'])
    add_neighbours('1', ['0', '9'])
    add_neighbours('2', ['3', '11'])
    add_neighbours('3', ['2', '4'])
    add_neighbours('4', ['3', '5','12'])
    add_neighbours('5', ['4', '13'])
    add_neighbours('6', ['16'])
    add_neighbours('7', ['18'])

    add_neighbours('8', ['0', '9'])
    add_neighbours('9', ['1','8','10','19'])
    add_neighbours('10', ['9', '11'])
    add_neighbours('11', ['2', '10', '20'])
    add_neighbours('12', ['4', '13', '22'])
    add_neighbours('13', ['5', '12', '14', '23'])
    add_neighbours('14', ['13', '15'])
    add_neighbours('15', ['14', '16'])
    add_neighbours('16', ['6', '15', '17','24',])
    add_neighbours('17', ['16', '18'])
    add_neighbours('18', ['7' , '17', '25'])
    add_neighbours('19', ['9', '27'])
    add_neighbours('20', ['11', '21'])
    add_neighbours('21', ['20', '22', '29'])
    add_neighbours('22', ['12', '21', '23', '30'])
    add_neighbours('23', ['13', '22'])
    add_neighbours('24', ['16', '33'])
    add_neighbours('25', ['18', '35'])

    add_neighbours('26', ['27'])
    add_neighbours('27', ['19', '26', '28'])
    add_neighbours('28', ['27', '37'])
    add_neighbours('29', ['21', '30'])
    add_neighbours('30', ['22', '29', '39'])
    add_neighbours('31', ['32', '41'])
    add_neighbours('32', ['31', '33'])
    add_neighbours('33', ['24', '32', '34'])
    add_neighbours('34', ['33', '35'])


    add_neighbours('35', ['25', '34', '36'])
    add_neighbours('36', ['35', '42'])

    add_neighbours('37', ['28', '38', '45'])
    add_neighbours('38', ['37'])
    add_neighbours('39', ['30', '40'])
    add_neighbours('40', ['39', '41', '47'])
    add_neighbours('41', ['31', '40', '48'])
    add_neighbours('42', ['36', '51'])

    add_neighbours('43', ['44'])
    add_neighbours('44', ['43', '45', '52'])
    add_neighbours('45', ['37', '44', '53'])
    add_neighbours('46', ['54'])
    add_neighbours('47', ['40', '48'])


    add_neighbours('48', ['47', '41', '55D'])
    #add_neighbours('48', ['41', '47', '55'])
    add_neighbours('49', ['50'])
    add_neighbours('50', ['49', '51'])
    add_neighbours('51', ['42','50','58'])


    add_neighbours('52', ['44', '53']) 
    add_neighbours('53', ['45', '52', '60']) 
    add_neighbours('54', ['46', '62'])  


    
    add_neighbours('55', ['48', '56', '65'])
    add_neighbours('56', ['55D', '57'])
    #add_neighbours('56', ['55', '57'])  
    add_neighbours('56', ['55', '57']) 
    add_neighbours('57', ['56', '66'])
    add_neighbours('58', ['51', '69'])

    add_neighbours('59', ['70'])
    add_neighbours('60', ['53', '61', '72'])
    add_neighbours('61', ['60', '62', '73'])
    add_neighbours('62', ['54', '61', '63','74'])
    add_neighbours('63', ['62', '64'])
    add_neighbours('64', ['63', '65'])

    add_neighbours('65', ['64', '55D', '75'])
    #add_neighbours('65', ['55', '64', '75'])
    add_neighbours('66', ['57', '67'])
    add_neighbours('67', ['66', '68'])
    add_neighbours('68', ['67', '69'])
    add_neighbours('69', ['58', '68', '76'])

    add_neighbours('70', ['59', '71'])
    add_neighbours('71', ['70', '72'])
    add_neighbours('72', ['60', '71', '73', '77'])
    add_neighbours('73', ['61', '72', '74', '78'])
    add_neighbours('74', ['62', '73', '79'])
    add_neighbours('75', ['65', '81'])
    add_neighbours('76', ['69', '86D'])
    #add_neighbours('76', ['69', '86'])

    add_neighbours('77', ['72', '78', '87'])
    add_neighbours('78', ['73', '77', '79'])
    add_neighbours('79', ['74', '78', '80'])
    add_neighbours('80', ['79', '88'])
    add_neighbours('81', ['75', '82', '90'])
    add_neighbours('82', ['81', '83'])
    add_neighbours('83', ['82', '84'])
    add_neighbours('84', ['83', '85'])

    add_neighbours('85', ['84', '91', '86D'])
    #add_neighbours('85', ['84', '86', '91'])
    add_neighbours('86', ['76', '85','92'])
    add_neighbours('87', ['77'])
    add_neighbours('88', ['80', '89'])
    add_neighbours('89', ['88', '90'])
    add_neighbours('90', ['81', '89'])
    add_neighbours('91', ['85', '92'])
    add_neighbours('92', ['91', '86D'])
    #add_neighbours('92', ['86', '91'])

    return graph_neighbours

def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list

graph_neighbours = generate_graph()