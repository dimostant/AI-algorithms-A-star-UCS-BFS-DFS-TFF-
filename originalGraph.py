graph_neighbours = {}

#the structure identifies each block as a unique number 
#starting the counter from 0 and going horizontally and skipping X's

def generate_graph():

    add_neighbours('0', ['1', '8'])
    add_neighbours('1', ['0', '9'])
    add_neighbours('2', ['3', '11'])
    add_neighbours('3', ['2', '4'])
    add_neighbours('4', ['3', '12','5'])
    add_neighbours('5', ['4', '13'])
    add_neighbours('6', ['16'])
    add_neighbours('7', ['18'])

    add_neighbours('8', ['0', '9'])
    add_neighbours('9', ['8', '1','19','10'])
    add_neighbours('10', ['9', '11'])
    add_neighbours('11', ['10', '2', '20'])
    add_neighbours('12', ['4', '22', '13'])
    add_neighbours('13', ['12', '5', '23', '14'])
    add_neighbours('14', ['13', '15'])
    add_neighbours('15', ['14', '16'])
    add_neighbours('16', ['15', '6', '24', '17'])
    add_neighbours('17', ['16', '18'])
    add_neighbours('18', ['17', '7', '25'])
    add_neighbours('19', ['9', '27'])
    add_neighbours('20', ['11', '21'])
    add_neighbours('21', ['20', '29','22'])
    add_neighbours('22', ['21', '12', '30', '23'])
    add_neighbours('23', ['22', '13'])
    add_neighbours('24', ['16', '33'])
    add_neighbours('25', ['18', '35'])

    add_neighbours('26', ['27'])
    add_neighbours('27', ['26', '19', '28'])
    add_neighbours('28', ['27', '37'])
    add_neighbours('29', ['21', '30'])
    add_neighbours('30', ['29', '39'])
    add_neighbours('31', ['41', '32'])
    add_neighbours('32', ['31', '33'])
    add_neighbours('33', ['32', '24', '34'])
    add_neighbours('34', ['33', '35'])
    add_neighbours('35', ['34', '25', '36'])
    add_neighbours('36', ['35', '42'])

    add_neighbours('37', ['28', '45', '38'])
    add_neighbours('38', ['37'])
    add_neighbours('39', ['30', '40'])
    add_neighbours('40', ['39', '47', '41'])
    add_neighbours('41', ['40', '31', '48'])
    add_neighbours('42', ['36', '51'])

    add_neighbours('43', ['44'])
    add_neighbours('44', ['43', '52', '45'])
    add_neighbours('45', ['44', '37', '53'])
    add_neighbours('46', ['54'])
    add_neighbours('47', ['40', '48'])
    add_neighbours('48', ['47', '41', '55'])
    #add_neighbours('48', ['47', '41', '55D'])
    add_neighbours('49', ['50'])
    add_neighbours('50', ['49', '51'])
    add_neighbours('51', ['50', '42', '58'])

    add_neighbours('52', ['44', '53']) 
    add_neighbours('53', ['45', '52']) 
    add_neighbours('54', ['46', '62'])  
    add_neighbours('55', ['48', '65', '56'])
    #add_neighbours('56', ['55D', '57']) 
    add_neighbours('56', ['55', '57']) 
    add_neighbours('57', ['56', '66'])
    add_neighbours('58', ['51', '69'])

    add_neighbours('59', ['70'])
    add_neighbours('60', ['53', '72', '61'])
    add_neighbours('61', ['60', '73', '62'])
    add_neighbours('62', ['61', '54', '74', '63'])
    add_neighbours('63', ['62', '64'])
    add_neighbours('64', ['63', '65'])
    #add_neighbours('65', ['64', '55D', '75'])
    add_neighbours('65', ['64', '55', '75'])
    add_neighbours('66', ['57', '67'])
    add_neighbours('67', ['66', '68'])
    add_neighbours('68', ['67', '69'])
    add_neighbours('69', ['68', '58', '76'])

    add_neighbours('70', ['59', '71'])
    add_neighbours('71', ['70', '72'])
    add_neighbours('72', ['71', '60', '77', '73'])
    add_neighbours('73', ['72', '61', '78', '74'])
    add_neighbours('74', ['73', '62', '79'])
    add_neighbours('75', ['65', '81'])
    #add_neighbours('76', ['69', '86D'])
    add_neighbours('76', ['69', '86'])

    add_neighbours('77', ['72', '87', '78'])
    add_neighbours('78', ['77', '73', '79'])
    add_neighbours('79', ['78', '79', '80'])
    add_neighbours('80', ['79', '88'])
    add_neighbours('81', ['75', '90', '82'])
    add_neighbours('82', ['81', '83'])
    add_neighbours('83', ['82', '84'])
    add_neighbours('84', ['83', '85'])
    #add_neighbours('85', ['84', '91', '86D'])
    add_neighbours('85', ['84', '91', '86'])
    add_neighbours('86', ['85', '76', '92'])

    add_neighbours('87', ['77'])
    add_neighbours('88', ['80', '89'])
    add_neighbours('89', ['88', '90'])
    add_neighbours('90', ['89', '81'])
    add_neighbours('91', ['85', '92'])
    #add_neighbours('92', ['91', '86D'])
    add_neighbours('92', ['91', '86'])

    return graph_neighbours

def add_neighbours(node, neighbours):
    new_list = []
    for val in neighbours:
        if val is not None and not val == '':
            new_list.append(str(val))
    graph_neighbours[str(node)] = new_list

graph_neighbours = generate_graph()