# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:32:44 2022

@author: luisa
"""

#file = open("C:\\Users\\luisa\\Documents\\Spring 2022\\Bio Structures\\PROJECT\\table.csv", "w+")
import csv
header = '''
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">      
    </head>
	<body>
    <div class="container-fluid" style="margin-top:2em">
'''

            
footer = '''
        </div>
    </body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</html>
'''

def create_html_table_from_csv(filename):
    columns = {
     'Uniprot ID':0,
     'Date':1,
     'RaptorX Prediction':2,
     'ligands':3,
     'raptx_rmsd_1':4,
     'raptx_rmsd_2':5,
     'raptx_rmsd_3':6,
     'raptx_rmsd_4':7,
     'raptx_rmsd_5':8,
     'raptx_af_rmsd_1':9,
     'raptx_af_rmsd_2':10,
     'raptx_af_rmsd_3':11,
     'raptx_af_rmsd_4':12,
     'raptx_af_rmsd_5':13,
    }
    csvfile = open(filename)
    file_content = csv.reader(csvfile, delimiter=',')
    content = '<div class="table-responsive"><table class="table table-dark table-hover">'
    modals = []
    index = 1
    skip_first = True
    for row in file_content:
        uid = row[columns['Uniprot ID']]
        date = row[columns['Date']]
        raptx = row[columns['RaptorX Prediction']]
        ligands = row[columns['ligands']]
        raptx_rmsd_1 = row[columns['raptx_rmsd_1']]
        raptx_rmsd_2 = row[columns['raptx_rmsd_2']]
        raptx_rmsd_3 = row[columns['raptx_rmsd_3']]
        raptx_rmsd_4 = row[columns['raptx_rmsd_4']]
        raptx_rmsd_5 = row[columns['raptx_rmsd_5']]
        raptx_af_rmsd_1 = row[columns['raptx_af_rmsd_1']]
        raptx_af_rmsd_2 = row[columns['raptx_af_rmsd_2']]
        raptx_af_rmsd_3 = row[columns['raptx_af_rmsd_3']]
        raptx_af_rmsd_4 = row[columns['raptx_af_rmsd_4']]
        raptx_af_rmsd_5 = row[columns['raptx_af_rmsd_5']]
        if index > 5:
            index = 1
        
        
         
        if not skip_first:
            modals.append(create_modal(uid,str(index)))
            index +=1
            uid_link = "https://www.uniprot.org/uniprot/"+uid
            link_tag_uid = '<a href="' + uid_link + '" target="_blank">'
            ligands_link = ''+ligands
            if ligands != 'N/A':
              ligands_link = '<a href="images/ronacaleret.png" target="_blank">'+ligands+'</a>'

            content+='''
                <tr>
                  <td>'''+link_tag_uid + uid +"</a>" +'''</td>
                  <td>'''+date+'''</td>
                  <td data-bs-toggle="modal" data-bs-target="#'''+uid+'''_modal"><u>View '''+uid+'''</u></td>
                  <td scope="col">'''+ ligands_link +'''</td>
                  <td scope="col">''' + raptx_rmsd_1 +'''</td>
                  <td scope="col">'''+ raptx_rmsd_2 +'''</td>
                  <td scope="col">''' + raptx_rmsd_3 +'''</td>
                  <td scope="col">'''+ raptx_rmsd_4 +'''</td>
                  <td scope="col">''' + raptx_rmsd_5 +'''</td>
                  <td scope="col">'''+ raptx_af_rmsd_1 +'''</td>
                  <td scope="col">'''+ raptx_af_rmsd_2 +'''</td>
                  <td scope="col">'''+ raptx_af_rmsd_3 +'''</td>
                  <td scope="col">'''+ raptx_af_rmsd_4 +'''</td>
                  <td scope="col">'''+ raptx_af_rmsd_5 +'''</td>
                </tr>
            '''
        else:
                content += '''
                 <thead>
                     <tr>
                     <th colspan="4"></th>
                      <th colspan="5">RaptorX Estimated RMSD</th>
                      <th colspan="5">RaptorX - AlphaFold RMSD</th>
                    </tr>
                    <tr>
                      <th scope="col">'''+ uid +'''</th>
                      <th scope="col">''' + date +'''</th>
                      <th scope="col">'''+ raptx +'''</th>
                      <th scope="col">'''+ ligands +'''</th>
                      <th scope="col">''' + raptx_rmsd_1 +'''</th>
                      <th scope="col">'''+ raptx_rmsd_2 +'''</th>
                      <th scope="col">''' + raptx_rmsd_3 +'''</th>
                      <th scope="col">'''+ raptx_rmsd_4 +'''</th>
                      <th scope="col">''' + raptx_rmsd_5 +'''</th>
                      <th scope="col">'''+ raptx_af_rmsd_1 +'''</th>
                      <th scope="col">'''+ raptx_af_rmsd_2 +'''</th>
                      <th scope="col">'''+ raptx_af_rmsd_3 +'''</th>
                      <th scope="col">'''+ raptx_af_rmsd_4 +'''</th>
                      <th scope="col">'''+ raptx_af_rmsd_5 +'''</th>
                    </tr>
                  </thead>
                  <tbody>
                    '''
                skip_first = False
            
            
    csvfile.close()
    
    for modal in modals:
        content+= modal
        
    content += '</tbody></table></div>'
        
    return content


def create_modal(uid,i):
    modal = '''
        <!-- Modal -->
        <div class="modal fade" id="'''+uid+'''_modal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-xl">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">'''+ uid +''' Model </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                '''+create_carousel(uid,i)+'''
              </div>
            </div>
          </div>
        </div>
    '''
    return modal

def create_carousel(uid,current_index):

    carousel = '''
 <div id="'''+uid+'_model'+current_index+'''" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">'''
    
    for i in range(5):    
        idx = i + 1
        active = ''
        if idx == 1:
            active = 'active'
        else:
            active = ''
        
        carousel_item = '''
      <div class="carousel-item '''+active+ '''">
        <img style="width:100%;height:600px" src="images/'''+uid+'''/'''+uid+'_model'+str(idx)+'''.png" class="d-block w-100" alt="...">
            <div class="carousel-caption d-none d-md-block">
                <h5>'''+uid+' Model '+str(idx)+'''</h5>
            </div>
        </div>
      
        '''
        carousel += carousel_item
       #end for loop 
       
    buttons = '''
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#'''+uid+'_model'+current_index+'''" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#'''+uid+'_model'+current_index+'''" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
    '''
    carousel += buttons
    return carousel
def print_page(header,content,footer):
    file = open('./index.html','w+')
    file.write(header + content + footer)
    file.close()
    
content = create_html_table_from_csv('../table.csv')
print_page(header,content,footer)