#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      john.f.kennedy
#
# Created:     30/01/2022
# Copyright:   (c) john.f.kennedy 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import arcpy
from arcpy import metadata as md
from time import time, localtime, strftime, sleep, gmtime
import xml.dom.minidom


def unique_values(table, field):  ##uses list comprehension
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({row[0] for row in cursor})


def main():
    try:
        function = "main()"
        print(function)

        localKeys =  [key for key in locals().keys() if "function" not in key]

        if localKeys:
            msg = "Local Keys: {0} in {1}".format(u", ".join(localKeys), function)
            print(msg); del msg
        del localKeys, function

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo

def prettyXML(metadata):
    try:
        dom = xml.dom.minidom.parse(metadata) # or xml.dom.minidom.parseString(xml_string)

        pretty_xml_as_string = dom.toprettyxml()

        lines = pretty_xml_as_string.split("\n")

        non_empty_lines = [line for line in lines if line.strip() != ""]

        string_without_empty_lines = ""

        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"

        #open(metadata, 'w').write(pretty_xml_as_string)
        open(metadata, 'w').write(string_without_empty_lines)

        del dom, pretty_xml_as_string, lines, non_empty_lines
        del string_without_empty_lines, line
        del metadata

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo

##
##def prettyXMLasString():
##    try:
##        print("prettyXMLasString()")
##        # Set a start time so that we can see how log things take
##        start_time = time()
##
##        metadata_xmls = ['Inport Interpolated Biomass Metadata.xml',
##                         'Inport Survey Locations Metadata.xml',
##                         'InPort Indicators Table Metadata.xml',
##                         'InPort DisMAP Regions Metadata.xml',
##                        ]
##
##        for metadata_xml in metadata_xmls:
##            #print(metadata_xml)
##            metadata = os.path.join(BASE_DIRECTORY, metadata_xml)
##            prettyXML(metadata)
##
##
##        # 'Inport Interpolated Biomass Metadata Template.xml'
##        #metadata_xml = os.path.join(BASE_DIRECTORY, 'Inport Interpolated Biomass Metadata.xml')
##
##        #prettyXML(metadata_xml)
##
##        # 'Inport Survey Locations Metadata Template.xml'
##        #metadata_xml = os.path.join(BASE_DIRECTORY, 'Inport Survey Locations Metadata.xml')
##
##        #prettyXML(metadata_xml)
##
##        # 'InPort Indicators Table Metadata.xml'
##        #metadata_xml = os.path.join(BASE_DIRECTORY, 'InPort Indicators Table Metadata.xml')
##
##        #prettyXML(metadata_xml)
##
##        # 'Inport DisMAP Regions Metadata.xml'
##        #metadata_xml = os.path.join(BASE_DIRECTORY, 'InPort DisMAP Regions Metadata.xml')
##
##        #prettyXML(metadata_xml)
##
##        # Elapsed time
##        end_time = time()
##        elapse_time =  end_time - start_time
##        msg = u"Elapsed Time {0} (H:M:S)\n".format(strftime("%H:%M:%S", gmtime(elapse_time)))
##        print(msg); del msg
##        del start_time, end_time, elapse_time
##
##        localKeys =  [key for key in locals().keys()]
##
##        if localKeys:
##            msg = "Local Keys: {0}".format(u", ".join(localKeys))
##            print(msg); del msg
##        del localKeys
##
##    except:
##        import sys, traceback
##        # Get the traceback object
##        tb = sys.exc_info()[2]
##        tbinfo = traceback.format_tb(tb)[0]
##        # Concatenate information together concerning the error into a message string
##        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
##        print(pymsg)
##        del pymsg, tb, tbinfo


def exportSelectedMetadata():
    try:
        function = "exportSelectedMetadata()"
        print("{0}".format(function))

        datasets = {
                     'AI' : 'DisMAP Interpolated Biomass Metadata.xml',
                     'Aleutian_Islands_Survey_Locations' : 'DisMAP Survey Locations Metadata.xml',
                     'Indicators' : 'DisMAP Indicators Table Metadata.xml',
                     'DisMAP_Regions' : 'DisMAP DisMAP Regions Metadata.xml',
                     #'AI_Shape' : 'DisMAP Aleutian Islands Region Boundary.xml',
                     'EPU_NOESTUARIES' : 'DisMap EPU Metadata.xml',
                   }

        for dataset in datasets:
            msg = "\t {0}".format(dataset)
            print(msg); del msg

            dataset_path = os.path.join(ProjectGDB, dataset)
            metadata = os.path.join(BASE_DIRECTORY, datasets[dataset])

            dataset_md = md.Metadata(dataset_path)

            msg = "\t\t Title: {0}".format(dataset_md.title)
            print(msg); del msg

            dataset_md.saveAsXML(metadata, 'REMOVE_ALL_SENSITIVE_INFO')

            prettyXML(metadata)

            del dataset_path, metadata, dataset_md

        localKeys =  [key for key in locals().keys() if 'function' not in key]

        if localKeys:
            msg = "Local Keys: {0} in {1}".format(u", ".join(localKeys), function)
            print(msg); del msg
        del localKeys, function

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo


def exportMetadata():
    try:
        function = "exportMetadata()"
        print("{0}".format(function))

        arcpy.env.workspace = ProjectGDB

##        datasets = list(set(arcpy.ListDatasets("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListFeatureClasses("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListRasters("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListTables("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListFiles("*{0}*".format(data_source_name)))
##                        )
        datasets = list(
                        #set(arcpy.ListDatasets("*")) |
                        #set(arcpy.ListFeatureClasses("*")) |
                        #set(arcpy.ListRasters("*")) |
                        #set(arcpy.ListTables("*"))
                        set(arcpy.ListFeatureClasses("*Survey_Locations"))
                       )

        for dataset in sorted(datasets):
            msg = "\t {0}".format(dataset)
            print(msg); del msg

            metadata = os.path.join(EXPORT_METADATA_DIRECTORY, "{0}.xml".format(dataset))

            dataset_md = md.Metadata(dataset)

            dataset_md.synchronize('ACCESSED', 1)
            #dataset_md.synchronize('ALWAYS')
            #dataset_md.synchronize('CREATED', 1)
            #dataset_md.synchronize('NOT_CREATED', 1)
            #dataset_md.synchronize('OVERWRITE')
            #dataset_md.synchronize('SELECTIVE')
            dataset_md.save()
            dataset_md.reload()

            if dataset_md.title:
                #dataset_md_title = dataset_md.title.replace('_', ' ')
                dataset_md_title = "{0} {1}".format(dataset.replace('_', ' '), DateCode)
                dataset_md.title = dataset_md_title
                dataset_md.save()
                dataset_md.reload()
                del dataset_md_title

            msg = "\t\t Title: {0}".format(dataset_md.title)
            print(msg); del msg

            msg = "\t\t Tags: {0}".format(dataset_md.tags)
            print(msg); del msg

            msg = "\t\t Summary: {0}".format(dataset_md.summary)
            print(msg); del msg

            msg = "\t\t Description: {0}".format(dataset_md.description)
            print(msg); del msg

            msg = "\t\t Credits: {0}".format(dataset_md.credits)
            print(msg); del msg

            # Delete all geoprocessing history and any thumbnails from the item's metadata
            if not dataset_md.isReadOnly:
                dataset_md.deleteContent('GPHISTORY')
                #dataset_md.deleteContent('THUMBNAIL')
                dataset_md.save()
                dataset_md.reload()

            #dataset_md.synchronize('ALWAYS')
            #dataset_md.synchronize('SELECTIVE')
            #dataset_md.saveAsXML(metadata, 'REMOVE_ALL_SENSITIVE_INFO')
            #dataset_md.saveAsXML(metadata, 'REMOVE_MACHINE_NAMES')
            dataset_md.saveAsXML(metadata)
            #dataset_md.exportMetadata(metadata,
            #                 metadata_removal_option='REMOVE_ALL_SENSITIVE_INFO')

            prettyXML(metadata)

            del metadata, dataset_md

        del datasets, dataset

        localKeys =  [key for key in locals().keys() if 'function' not in key]

        if localKeys:
            msg = "Local Keys: {0} in {1}()".format(u", ".join(localKeys), function)
            print(msg); del msg
        del localKeys, function

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo

def updateMetadata():
    try:
        function = "updateMetadata()"
        print("{0}".format(function))

        arcpy.env.workspace = ProjectGDB

##        datasets = list(set(arcpy.ListDatasets("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListFeatureClasses("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListRasters("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListTables("*{0}*".format(data_source_name))) |
##                        set(arcpy.ListFiles("*{0}*".format(data_source_name)))
##                        )
        datasets = list(
                        #set(arcpy.ListDatasets("*")) |
                        #set(arcpy.ListFeatureClasses("*")) |
                        #set(arcpy.ListRasters("*")) |
                        #set(arcpy.ListTables("*"))
                        set(arcpy.ListFeatureClasses("*Survey_Locations"))
                       )

        for dataset in sorted(datasets):
            msg = "\t {0}".format(dataset)
            print(msg); del msg

            metadata = os.path.join(EXPORT_METADATA_DIRECTORY, "{0}.xml".format(dataset))
            dataset_md = md.Metadata(metadata)

##            dataset_md = md.Metadata(dataset)
##            dataset_md.synchronize('ACCESSED', 1)
##            #dataset_md.synchronize('ALWAYS')
##            #dataset_md.synchronize('CREATED', 1)
##            #dataset_md.synchronize('NOT_CREATED', 1)
##            #dataset_md.synchronize('OVERWRITE')
##            #dataset_md.synchronize('SELECTIVE')
##            dataset_md.save()
##            dataset_md.reload()
##
##            if dataset_md.title:
##                #dataset_md_title = dataset_md.title.replace('_', ' ')
##                dataset_md_title = "{0} {1}".format(dataset.replace('_', ' '), DateCode)
##                dataset_md.title = dataset_md_title
##                dataset_md.save()
##                dataset_md.reload()
##                del dataset_md_title

            msg = "\t\t Title: {0}".format(dataset_md.title)
            print(msg); del msg

            msg = "\t\t Tags: {0}".format(dataset_md.tags)
            print(msg); del msg

            msg = "\t\t Summary: {0}".format(dataset_md.summary)
            print(msg); del msg

            msg = "\t\t Description: {0}".format(dataset_md.description)
            print(msg); del msg

            msg = "\t\t Credits: {0}".format(dataset_md.credits)
            print(msg); del msg

##            # Delete all geoprocessing history and any thumbnails from the item's metadata
##            if not dataset_md.isReadOnly:
##                dataset_md.deleteContent('GPHISTORY')
##                #dataset_md.deleteContent('THUMBNAIL')
##                dataset_md.save()
##                dataset_md.reload()

            #dataset_md.synchronize('ALWAYS')
            #dataset_md.synchronize('SELECTIVE')
            #dataset_md.saveAsXML(metadata, 'REMOVE_ALL_SENSITIVE_INFO')
            #dataset_md.saveAsXML(metadata, 'REMOVE_MACHINE_NAMES')
            #dataset_md.saveAsXML(metadata)


            selective_metadata = os.path.join(EXPORT_METADATA_DIRECTORY, "{0} SELECTIVE.xml".format(dataset))

            dataset_md.saveAsXML(selective_metadata)

            del metadata, dataset_md

            selective_md = md.Metadata(selective_metadata)


            #selective_md.synchronize('ACCESSED', 1)
            #selective_md.synchronize('ALWAYS')
            selective_md.synchronize('CREATED', 1)
            #selective_md.synchronize('NOT_CREATED', 1)
            #selective_md.synchronize('OVERWRITE')
            #selective_md.synchronize('SELECTIVE')

            import_selective_metadata = r'C:\Users\john.f.kennedy\Documents\GitHub\DisMap\ArcGIS Analysis\March 7 2022\ArcGIS Metadata March 7 2022 Dev\Survey Locations Metadata.xml'
            selective_md.importMetadata(import_selective_metadata)
            selective_md.save()


            prettyXML(selective_metadata)

            del selective_metadata, selective_md, import_selective_metadata

        del datasets, dataset

        localKeys =  [key for key in locals().keys() if 'function' not in key]

        if localKeys:
            msg = "Local Keys: {0} in {1}()".format(u", ".join(localKeys), function)
            print(msg); del msg
        del localKeys, function

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo


def createEmptyTempMetadataXML():
    try:
        function = "createEmptyTempMetadataXML()"
        print(function)

        empty_xml = os.path.join(EXPORT_METADATA_DIRECTORY, "empty.xml")
        temp_xml = os.path.join(EXPORT_METADATA_DIRECTORY, "temp.xml")

        # Create a new Metadata object and add some content to it
        new_md = md.Metadata()
        # Empty XML Files
        new_md.saveAsXML(empty_xml)

        # Temp XML File
        new_md.title = 'My Title'
        new_md.tags = 'Tag1, Tag2'
        new_md.summary = 'My Summary'
        new_md.description = 'My Description'
        new_md.credits = 'My Credits'
        new_md.accessConstraints = 'My Access Constraints'
        new_md.saveAsXML(temp_xml)

##        # Assign the Metadata object's content to a target item
##        streets_path = r'C:\Data\LocalArea.gdb\Streets'
##        tgt_item_md = md.Metadata(streets_path)
##        if not tgt_item_md.isReadOnly:
##            tgt_item_md.copy(new_md)
##            tgt_item_md.save()

        prettyXML(empty_xml)
        prettyXML(temp_xml)

        del empty_xml, temp_xml, new_md

        localKeys =  [key for key in locals().keys() if "function" not in key]

        if localKeys:
            msg = "Local Keys: {0} in {1}".format(u", ".join(localKeys), function)
            print(msg); del msg
        del localKeys, function

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo


def exportInportMetadata():
    try:
        print("exportInportMetadata()")

        # make sure the name of the xsl style sheet is up-to-date
        mainXslFilename = "ArcGIS2InportV07.xsl"

        #if not os.path.isdir(workspacepath+"/Export Metadata/"):
        #    os.makedirs(workspacepath+"/Export Metadata/")

        # before running this notebook, you set the required constants below
        #
        # defaultEffectiveDate is always required. Example 2018-06
        #    - defaultEffectiveDate (effective dates for contacts - there is no where to enter this in metadata so it must be entered in the xslt file)
        # one of these is always required
        #    - parentCatalogItemId (use when creating a new inport record, leave blank '' when updating an inport record)
        #    - catalogItemId (use when updating an inport record, leave blank '' when creating a new inport record)
        # the following are only needed if you do not provide these contacts directly in your metadata
        #    - defaultPointOfContactEmail (in ArcGIS Pro metadata, define this contact in Resource>Points of Contact)
        #    - defaultDataStewardEmail (in ArcGIS Pro metadata, define this contact in Overview>Citation Contacts)
        #    - defaultMetadataContactEmail (in ArcGIS Pro metadata, define this contact in Metadata>Contacts)
        #    - defaultOrganizationName (in ArcGIS Pro metadata, define this contact in Resource>Distribution>Distributor )

        parameters = {
            'defaultEffectiveDate':"2022-03-07",
            'parentCatalogItemId':"",
            'catalogItemId':"",
            #'defaultPointOfContactEmail':"pointofcontact@noaa.gov",
            'defaultPointOfContactEmail':"melissa.karp@noaa.gov",
            #'defaultDataStewardEmail':"datasteward@noaa.gov",
            'defaultDataStewardEmail':"tim.haverlandd@noaa.gov",
            #'defaultMetadataContactEmail':"metadata@noaa.gov",
            'defaultMetadataContactEmail':"john.f.kennedy@noaa.gov",
            #'defaultOrganizationName':"Default OrgName",
            'defaultOrganizationName':"NMFS Office of Science and Technology",
            }

##        # Read in the xsl file and replace the parameter values
##        #with open(xslTemplatePath+"\\"+mainXslFilename, 'r') as file :
##        with open(BASE_DIRECTORY+"\\ArcGIS2InPort\\"+mainXslFilename, 'r') as file:
##            filedata = file.read()
##
##        for k in parameters:
##            # Replace the target string
##            filedata = filedata.replace("["+k+"]", parameters[k])
##            del k
##        del parameters
##
##        # Write the file out again to the workspace folder
##        with open(BASE_DIRECTORY+"\\"+mainXslFilename, 'w') as file:
##            file.write(filedata)
##            del file, filedata

##        datasets = { 'AI' : 'InPort Interpolated Biomass Metadata.xml',
##                     'Aleutian_Islands_Survey_Locations' : 'InPort Survey Locations Metadata.xml',
##                     'Indicators' : 'InPort Indicators Table Metadata.xml',
##                     'DisMAP_Regions' : 'InPort DisMAP Regions Metadata.xml',
##                   }
        datasets = { 'DisMap Interpolated Biomass Metadata.xml' : ['InPort Interpolated Biomass Metadata.xml', "66897"],
                     'DisMap Survey Locations Metadata.xml' : ['InPort Survey Locations Metadata.xml', "66891"],
                     'DisMap Indicators Table Metadata.xml' : ['InPort Indicators Table Metadata.xml', "66901"],
                     'DisMap DisMAP Regions Metadata.xml' : ['InPort DisMAP Regions Metadata.xml', "66893"],
                     'DisMap EPU Metadata.xml' : ['InPort EPU Metadata.xml', '67001'],
                   }

        for dataset in datasets:
            msg = "\t {0}".format(dataset)
            print(msg); del msg

            parameters['catalogItemId'] = datasets[dataset][1]

            # Read in the xsl file and replace the parameter values
            #with open(xslTemplatePath+"\\"+mainXslFilename, 'r') as file :
            with open(BASE_DIRECTORY+"\\ArcGIS2InPort\\"+mainXslFilename, 'r') as file:
                filedata = file.read()

            for k in parameters:
                # Replace the target string
                filedata = filedata.replace("["+k+"]", parameters[k])
                del k

            # Write the file out again to the workspace folder
            with open(BASE_DIRECTORY+"\\"+mainXslFilename, 'w') as file:
                file.write(filedata)
                del file, filedata

            #dataset_path = os.path.join(ProjectGDB, dataset)
            dataset_path = os.path.join(BASE_DIRECTORY, dataset)
            #metadata = os.path.join(BASE_DIRECTORY, datasets[dataset])
            metadata = os.path.join(BASE_DIRECTORY, datasets[dataset][0])

            dataset_md = md.Metadata(dataset_path)

            msg = "\t\t Title: {0}".format(dataset_md.title)
            print(msg); del msg

            dataset_md.exportMetadata(metadata, "CUSTOM", "EXACT_COPY", BASE_DIRECTORY+"/"+mainXslFilename)

            prettyXML(metadata)

            del dataset_path, metadata, dataset_md

        del parameters

        if os.path.isfile(BASE_DIRECTORY+"\\"+mainXslFilename) or os.path.islink(BASE_DIRECTORY+"\\"+mainXslFilename):
            os.unlink(BASE_DIRECTORY+"\\"+mainXslFilename)

        del  datasets, dataset, mainXslFilename

        localKeys =  [key for key in locals().keys()]

        if localKeys:
            msg = "Local Keys: {0}".format(u", ".join(localKeys))
            print(msg); del msg
        del localKeys

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo


def exportInportEntityMetadata():
    try:
        print("exportInportEntityMetadata()")

        # make sure the name of the xsl style sheet is up-to-date
        entityXslFilename = "ArcGIS2InPort_entityV02.xsl"

        # before running this notebook, you set the required constants below:
        #    - parentCatalogItemId (use when creating a new inport record, leave blank "" when updating an inport record)
        #    - catalogItemId (use when updating an inport record, leave blank "" when creating a new inport record)

        parameters = {
            'parentCatalogItemId':"",
            'catalogItemId':"",
        }

##        # Read in the xsl file and replace the parameter values
##        with open(BASE_DIRECTORY+"\\ArcGIS2InPort\\"+entityXslFilename, 'r') as file:
##            filedata = file.read()
##
##        for k in parameters:
##            # Replace the target string
##            filedata = filedata.replace("["+k+"]", parameters[k])
##            del k
##        del parameters
##
##        # Write the file out again to the workspace folder
##        with open(BASE_DIRECTORY+"\\"+entityXslFilename, 'w') as file:
##            file.write(filedata)
##            del file, filedata

##        datasets = { 'AI' : 'InPort Interpolated Biomass Entity Metadata.xml',
##                     'Aleutian_Islands_Survey_Locations' : 'InPort Survey Locations Entity Metadata.xml',
##                     'Indicators' : 'InPort Indicators Table Entity Metadata.xml',
##                     'DisMAP_Regions' : 'InPort DisMAP Regions Entity Metadata.xml',
##                   }

        datasets = { 'DisMap Interpolated Biomass Metadata.xml' : ['InPort Interpolated Biomass Metadata Entity.xml', "66898"],
                     'DisMap Survey Locations Metadata.xml' : ['InPort Survey Locations Metadata Entity.xml', "66892"],
                     'DisMap Indicators Table Metadata.xml' : ['InPort Indicators Table Metadata Entity.xml', "66902"],
                     'DisMap DisMAP Regions Metadata.xml' : ['InPort DisMAP Regions Metadata Entity.xml', "66894"],
                     'DisMap EPU Metadata.xml' : ['InPort EPU Metadata Entity.xml', ''],
                   }

        for dataset in datasets:
            msg = "\t {0}".format(dataset)
            print(msg); del msg

            parameters['catalogItemId'] = datasets[dataset][1]

            # Read in the xsl file and replace the parameter values
            with open(BASE_DIRECTORY+"\\ArcGIS2InPort\\"+entityXslFilename, 'r') as file:
                filedata = file.read()

            for k in parameters:
                # Replace the target string
                filedata = filedata.replace("["+k+"]", parameters[k])
                del k

            # Write the file out again to the workspace folder
            with open(BASE_DIRECTORY+"\\"+entityXslFilename, 'w') as file:
                file.write(filedata)
                del file, filedata

            #dataset_path = os.path.join(ProjectGDB, dataset)
            dataset_path = os.path.join(BASE_DIRECTORY, dataset)
            #metadata = os.path.join(BASE_DIRECTORY, datasets[dataset])
            metadata = os.path.join(BASE_DIRECTORY, datasets[dataset][0])

            dataset_md = md.Metadata(dataset_path)

            msg = "\t\t Title: {0}".format(dataset_md.title)
            print(msg); del msg

            dataset_md.exportMetadata(metadata, "CUSTOM", "EXACT_COPY", BASE_DIRECTORY+"/"+entityXslFilename)

            prettyXML(metadata)

            del dataset_path, metadata, dataset_md

        del parameters

        if os.path.isfile(BASE_DIRECTORY+"\\"+entityXslFilename) or os.path.islink(BASE_DIRECTORY+"\\"+entityXslFilename):
            os.unlink(BASE_DIRECTORY+"\\"+entityXslFilename)

        del  datasets, dataset, entityXslFilename

        localKeys =  [key for key in locals().keys()]

        if localKeys:
            msg = "Local Keys: {0}".format(u", ".join(localKeys))
            print(msg); del msg
        del localKeys

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo


##def saveInportTemplateMetadata():
##    try:
##        print("saveInportTemplateMetadata()")
##        # Set a start time so that we can see how log things take
##        start_time = time()
##
##        # Set Workspace
##        arcpy.env.workspace = ProjectGDB
##        # Set Scratch Workspace
##        arcpy.env.scratchWorkspace = ScratchGDB
##
##        # Get the item's Metadata object
##        mosaic_path = os.path.join(ProjectGDB, 'AI')
##        mosaic_md = md.Metadata(mosaic_path)
##        del mosaic_path
##
##        msg = "Title: {0}".format(mosaic_md.title)
##        print(msg); del msg
##
##        # Save a copy of the item's metadata to an xml file as a backup.
##        # This copy is for internal use only.
##        target_copy_path = os.path.join(BASE_DIRECTORY, 'Inport Interpolated Biomass Metadata.xml')
##        mosaic_md.saveAsXML(target_copy_path, 'REMOVE_ALL_SENSITIVE_INFO')
##
##        prettyXML(target_copy_path)
##
##        del target_copy_path, mosaic_md
##
##        # Get the item's Metadata object
##        survey_locations_path = os.path.join(ProjectGDB, 'Aleutian_Islands_Survey_Locations')
##        survey_locations_md = md.Metadata(survey_locations_path)
##        del survey_locations_path
##
##        msg = "Title: {0}".format(survey_locations_md.title)
##        print(msg); del msg
##
##        # Save a copy of the item's metadata to an xml file as a backup.
##        # This copy is for internal use only.
##        target_copy_path = os.path.join(BASE_DIRECTORY, 'Inport Survey Locations Metadata.xml')
##        survey_locations_md.saveAsXML(target_copy_path, 'REMOVE_ALL_SENSITIVE_INFO')
##
##        prettyXML(target_copy_path)
##
##        del target_copy_path, survey_locations_md
##
##        # Get the item's Metadata object
##        dismap_regions_path = os.path.join(ProjectGDB, 'DisMAP_Regions')
##        dismap_regions_md = md.Metadata(dismap_regions_path)
##        del dismap_regions_path
##
##        msg = "Title: {0}".format(dismap_regions_md.title)
##        print(msg); del msg
##
##        # Save a copy of the item's metadata to an xml file as a backup.
##        # This copy is for internal use only.
##        target_copy_path = os.path.join(BASE_DIRECTORY, 'Inport DisMAP Regions Metadata.xml')
##        dismap_regions_md.saveAsXML(target_copy_path, 'REMOVE_ALL_SENSITIVE_INFO')
##
##        prettyXML(target_copy_path)
##
##        del target_copy_path, dismap_regions_md
##
##        # Get the item's Metadata object
##        indicators_path = os.path.join(ProjectGDB, 'Indicators')
##        indicators_md = md.Metadata(indicators_path)
##        del indicators_path
##
##        msg = "Title: {0}".format(indicators_md.title)
##        print(msg); del msg
##
##        # Save a copy of the item's metadata to an xml file as a backup.
##        # This copy is for internal use only.
##        target_copy_path = os.path.join(BASE_DIRECTORY, 'InPort Indicators Table Metadata.xml')
##        indicators_md.saveAsXML(target_copy_path, 'REMOVE_ALL_SENSITIVE_INFO')
##
##        prettyXML(target_copy_path)
##
##        del target_copy_path, indicators_md
##
##        # Elapsed time
##        end_time = time()
##        elapse_time =  end_time - start_time
##        msg = u"Elapsed Time {0} (H:M:S)\n".format(strftime("%H:%M:%S", gmtime(elapse_time)))
##        print(msg); del msg
##        del start_time, end_time, elapse_time
##
##        localKeys =  [key for key in locals().keys()]
##
##        if localKeys:
##            msg = "Local Keys: {0}".format(u", ".join(localKeys))
##            print(msg); del msg
##        del localKeys
##
##    except:
##        import sys, traceback
##        # Get the traceback object
##        tb = sys.exc_info()[2]
##        tbinfo = traceback.format_tb(tb)[0]
##        # Concatenate information together concerning the error into a message string
##        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
##        print(pymsg)
##        del pymsg, tb, tbinfo


def importTemplateMetadata():
    try:
        print("importTemplateMetadata()")
        # Set a start time so that we can see how log things take
        start_time = time()

        # Set Workspace
        arcpy.env.workspace = ProjectGDB
        # Set Scratch Workspace
        arcpy.env.scratchWorkspace = ScratchGDB

        #mosaic_template_path = os.path.join(BASE_DIRECTORY, 'Inport Interpolated Biomass Metadata Template.xml')
        mosaic_template_path = os.path.join(BASE_DIRECTORY, 'DisMAP Interpolated Biomass Metadata.xml')

        #survey_locations_template_path = os.path.join(BASE_DIRECTORY, 'Inport Survey Locations Metadata Template.xml')
        survey_locations_template_path = os.path.join(BASE_DIRECTORY, 'DisMAP Survey Locations Metadata.xml')

        # 'InPort Indicators Table Metadata.xml'
        indicators_template_path = os.path.join(BASE_DIRECTORY, 'DisMAP Indicators Table Metadata.xml')

        # 'Inport DisMAP Regions Metadata.xml'
        dismap_regions_template_path = os.path.join(BASE_DIRECTORY, 'DisMAP DisMAP Regions Metadata.xml')

        # 'DisMap EPU Metadata.xml' : ['InPort EPU Metadata.xml', ''],
        epu_template_path = os.path.join(BASE_DIRECTORY, 'DisMap EPU Metadata.xml')

        indicators_md = md.Metadata('Indicators')

        msg = "\t Metadata Title: {0}".format(indicators_md.title)
        print(msg); del msg

        # Import the standard-format metadata content to the target item
        if not indicators_md.isReadOnly:
            # Synchronize the item's metadata now
            #indicators_md.synchronize('ALWAYS')
            indicators_md.synchronize('SELECTIVE')
            indicators_md.importMetadata(indicators_template_path)
            indicators_md.save()

        del indicators_md, indicators_template_path

        dismap_regions_md = md.Metadata('DisMAP_Regions')

        msg = "\t Metadata Title: {0}".format(dismap_regions_md.title)
        print(msg); del msg

        # Import the standard-format metadata content to the target item
        if not dismap_regions_md.isReadOnly:
            # Synchronize the item's metadata now
            #dismap_regions_md.synchronize('ALWAYS')
            dismap_regions_md.synchronize('SELECTIVE')
            dismap_regions_md.importMetadata(dismap_regions_template_path)
            dismap_regions_md.save()

        del dismap_regions_md, dismap_regions_template_path

        epu_md = md.Metadata('EPU_NOESTUARIES')

        msg = "\t Metadata Title: {0}".format(epu_md.title)
        print(msg); del msg

        # Import the standard-format metadata content to the target item
        if not epu_md.isReadOnly:
            # Synchronize the item's metadata now
            #epu_md.synchronize('ALWAYS')
            epu_md.synchronize('SELECTIVE')
            epu_md.importMetadata(epu_template_path)
            epu_md.save()

        del epu_md, epu_template_path

        # Start looping over the table_name array as we go region by region.
        for table_name in table_names:
            # Assigning variables from items in the chosen table list
            #region_shape = table_name[0]
            #region_boundary = table_name[1]
            region_abb = table_name[2]
            region = table_name[3]
            csv_file = table_name[4]
            #region_georef = table_name[5]
            #region_contours = table_name[6]

            # Make Geodatabase friendly name
            region_name = region.replace('(','').replace(')','').replace('-','_to_').replace(' ', '_')

            # Write a message to the log file
            msg = "STARTING REGION {0} ON {1}".format(region, strftime("%a %b %d %I:%M:%S %p", localtime()))
            print(msg); del msg

            #print(region)
            #print(region_abb)
            #print(region_name)
            #print(csv_file)

            mosaic_md = md.Metadata(region_abb)

            msg = "\t Metadata Title: {0}".format(mosaic_md.title)
            print(msg); del msg

            # Import the standard-format metadata content to the target item
            if not mosaic_md.isReadOnly:
                # Synchronize the item's metadata now
                #mosaic_md.synchronize('ALWAYS')
                mosaic_md.synchronize('SELECTIVE')
                mosaic_md.importMetadata(mosaic_template_path)
                mosaic_md.save()

            del mosaic_md

            survey_locations_md = md.Metadata("{0}_Survey_Locations".format(region_name))

            msg = "\t Metadata Title: {0}".format(survey_locations_md.title)
            print(msg); del msg

            # Import the standard-format metadata content to the target item
            if not survey_locations_md.isReadOnly:
                #survey_locations_md.synchronize('ALWAYS')
                survey_locations_md.synchronize('SELECTIVE')
                survey_locations_md.importMetadata(survey_locations_template_path)
                survey_locations_md.save()

            del survey_locations_md

            #Final benchmark for the region.
            msg = "ENDING REGION {} COMPLETED ON {}".format(region, strftime("%a %b %d %I:%M:%S %p", localtime()))
            print(msg); del msg

            del table_name, region_abb, region, csv_file, region_name

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        msg = u"Elapsed Time {0} (H:M:S)\n".format(strftime("%H:%M:%S", gmtime(elapse_time)))
        print(msg); del msg
        del start_time, end_time, elapse_time

        del mosaic_template_path, survey_locations_template_path

        localKeys =  [key for key in locals().keys()]

        if localKeys:
            msg = "Local Keys: {0}".format(u", ".join(localKeys))
            print(msg); del msg
        del localKeys

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo


def importCrfMetadata():
    try:
        print("importCrfMetadata()")
        # Set a start time so that we can see how log things take
        start_time = time()

        # Set Workspace
        #arcpy.env.workspace = ProjectGDB
        # Set Scratch Workspace
        #arcpy.env.scratchWorkspace = ScratchGDB

        mosaic_template_path = os.path.join(BASE_DIRECTORY, 'DisMAP Interpolated Biomass Metadata.xml')

        arcpy.env.workspace = MOSAIC_DIRECTORY

        crfs = arcpy.ListRasters()

        for crf in crfs:

            tmp_metadata = os.path.join(MOSAIC_DIRECTORY, "tmp_metadata.xml")
            empty_metadata = os.path.join(BASE_DIRECTORY, 'DisMap Empty.xml')

            mosaic_md = md.Metadata(crf)

            msg = "\t Metadata Title: {0}".format(mosaic_md.title)
            print(msg); del msg

            mosaic_md.saveAsXML(tmp_metadata, 'REMOVE_ALL_SENSITIVE_INFO')

            prettyXML(tmp_metadata)

            # Import the standard-format metadata content to the target item
            if not mosaic_md.isReadOnly:
                # Synchronize the item's metadata now
                mosaic_md.synchronize('ALWAYS')
                mosaic_md.save()
                mosaic_md.reload()
                msg = "\t Metadata Title: {0}".format(mosaic_md.title)
                print(msg); del msg
                #mosaic_md.synchronize('OVERWRITE')
                #mosaic_md.synchronize('SELECTIVE')
                mosaic_md.importMetadata(empty_metadata)
                mosaic_md.save()
                mosaic_md.synchronize('SELECTIVE')
                mosaic_md.importMetadata(tmp_metadata)
                mosaic_md.save()
                mosaic_md.synchronize('SELECTIVE')
                mosaic_md.importMetadata(mosaic_template_path)
                msg = "\t Metadata Title: {0}".format(mosaic_md.title)
                print(msg); del msg
                mosaic_md.synchronize('ALWAYS')
                msg = "\t Metadata Title: {0}".format(mosaic_md.title)
                print(msg); del msg
                mosaic_md.save()

##            del mosaic_md
##
##            mosaic_md = md.Metadata(crf)
##
##            # Import the standard-format metadata content to the target item
##            if not mosaic_md.isReadOnly:
##                # Synchronize the item's metadata now
##                mosaic_md.synchronize('ALWAYS')
##                #mosaic_md.synchronize('OVERWRITE')
##                #mosaic_md.synchronize('SELECTIVE')
##                mosaic_md.importMetadata(mosaic_template_path)
##                mosaic_md.save()

            #if os.path.isfile(tmp_metadata) or os.path.islink(tmp_metadata):
            #    os.unlink(tmp_metadata)

            del mosaic_md, crf, tmp_metadata

        del crfs, mosaic_template_path

        # Elapsed time
        end_time = time()
        elapse_time =  end_time - start_time
        msg = u"Elapsed Time {0} (H:M:S)\n".format(strftime("%H:%M:%S", gmtime(elapse_time)))
        print(msg); del msg
        del start_time, end_time, elapse_time

        localKeys =  [key for key in locals().keys()]

        if localKeys:
            msg = "Local Keys: {0}".format(u", ".join(localKeys))
            print(msg); del msg
        del localKeys

    except:
        import sys, traceback
        # Get the traceback object
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        # Concatenate information together concerning the error into a message string
        pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
        print(pymsg)
        del pymsg, tb, tbinfo


if __name__ == '__main__':
    # Use all of the cores on the machine.
    arcpy.env.parallelProcessingFactor = "100%"
    ##!!WARNING!!:::::::SET THE OVERWRITE TO ON - ANY ITEMS THAT GET SAVED WILL BE OVERWRITTEN
    arcpy.env.overwriteOutput = True

    # Project related items

    # May 4 2022
    #Version = "May 4 2022"
    #DateCode = "20220504"

    # March 7 2022
    Version = "March 7 2022"
    DateCode = "20220307"

    # March 1 2022
    #Version = "March 1 2022"
    #DateCode = "20220301"

    # February 1 2022
    #Version = "February 1 2022"
    #DateCode = "20220201"

    # March 1 2021
    #Version = "March 1 2021"
    #DateCode = "20210301"

    ProjectName = "DisMAP {0}".format(Version)

    BASE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    BASE_DIRECTORY = os.path.join(BASE_DIRECTORY, Version)
    # print('BASE_DIRECTORY: ', BASE_DIRECTORY)

    # ###--->>> Software Environment Level
    #SoftwareEnvironmentLevel = ""
    SoftwareEnvironmentLevel = "Dev"
    #SoftwareEnvironmentLevel = "Test"

    ProjectGDB = os.path.join(BASE_DIRECTORY, "{0}.gdb".format(ProjectName + " " + SoftwareEnvironmentLevel))
    ANALYSIS_DIRECTORY = os.path.join(BASE_DIRECTORY, "Analysis Folder {0} {1}".format(Version, SoftwareEnvironmentLevel))
    MOSAIC_DIRECTORY = os.path.join(BASE_DIRECTORY, "Mosaic Folder {0} {1}".format(Version, SoftwareEnvironmentLevel))
    EXPORT_METADATA_DIRECTORY = os.path.join(BASE_DIRECTORY, "Export Metadata {0} {1}".format(Version, SoftwareEnvironmentLevel))
    ARCGIS_METADATA_DIRECTORY = os.path.join(BASE_DIRECTORY, "ArcGIS Metadata {0} {1}".format(Version, SoftwareEnvironmentLevel))
    INPORT_METADATA_DIRECTORY = os.path.join(BASE_DIRECTORY, "InPort Metadata {0} {1}".format(Version, SoftwareEnvironmentLevel))
    ScratchGDB = os.path.join(BASE_DIRECTORY, "Scratch {0} {1}".format(Version, SoftwareEnvironmentLevel), "scratch.gdb")
    ScratchFolder = os.path.join(BASE_DIRECTORY, "Scratch {0} {1}".format(Version, SoftwareEnvironmentLevel))

    if not os.path.isdir(EXPORT_METADATA_DIRECTORY): os.makedirs(EXPORT_METADATA_DIRECTORY)

    if not os.path.isdir(ARCGIS_METADATA_DIRECTORY): os.makedirs(ARCGIS_METADATA_DIRECTORY)

    if not os.path.isdir(INPORT_METADATA_DIRECTORY): os.makedirs(INPORT_METADATA_DIRECTORY)

    arcpy.env.scratchWorkspace = ScratchGDB

    table_names = [
                   [ 'AI_Shape', 'AI_Boundary','AI', 'Aleutian Islands', 'ai_csv', 'NAD_1983_2011_UTM_Zone_1N', 'contour_ai'],
                   [ 'EBS_Shape', 'EBS_Boundary','EBS', 'Eastern Bering Sea', 'ebs_csv', 'NAD_1983_2011_UTM_Zone_3N', 'contour_ebs'],
                   [ 'GOA_Shape', 'GOA_Boundary','GOA', 'Gulf of Alaska', 'goa_csv', 'NAD_1983_2011_UTM_Zone_5N', 'contour_goa'],

                   [ 'GOM_Shape', 'GOM_Boundary','GOM', 'Gulf of Mexico', 'gmex_csv', 'NAD_1983_2011_UTM_Zone_15N', 'contour_gom'],

                   [ 'NEUS_Fall_Shape', 'NEUS_Fall_Boundary','NEUS_F', 'Northeast US Fall', 'neusf_csv', 'NAD_1983_2011_UTM_Zone_18N', 'contour_neus'],
                   [ 'NEUS_Spring_Shape', 'NEUS_Spring_Boundary','NEUS_S', 'Northeast US Spring', 'neus_csv', 'NAD_1983_2011_UTM_Zone_18N', 'contour_neus'],


                   [ 'SEUS_Shape', 'SEUS_Boundary','SEUS_SPR', 'Southeast US Spring', 'seus_spr_csv', 'NAD_1983_2011_UTM_Zone_17N', 'contour_seus'],
                   [ 'SEUS_Shape', 'SEUS_Boundary','SEUS_SUM', 'Southeast US Summer', 'seus_sum_csv', 'NAD_1983_2011_UTM_Zone_17N', 'contour_seus'],
                   [ 'SEUS_Shape', 'SEUS_Boundary','SEUS_FALL', 'Southeast US Fall', 'seus_fal_csv', 'NAD_1983_2011_UTM_Zone_17N', 'contour_seus'],

                   [ 'WC_Ann_Shape', 'WC_Ann_Boundary','WC_ANN', 'West Coast Annual 2003-Present', 'wcann_csv', 'NAD_1983_2011_UTM_Zone_10N', 'contour_wc'],
                   [ 'WC_Tri_Shape', 'WC_Tri_Boundary','WC_TRI', 'West Coast Triennial 1977-2004', 'wctri_csv', 'NAD_1983_2011_UTM_Zone_10N', 'contour_wc']
                  ]

    #regions = ['Aleutian Islands', 'Eastern Bering Sea', 'Gulf of Alaska', 'Gulf of Mexico', 'Northeast US Fall',
    #           'Southeast US Fall', 'Northeast US Spring', 'Southeast US Spring', 'Southeast US Summer',
    #           'West Coast Annual 2003-Present', 'West Coast Triennial 1977-2004']

    # Set to True if we want to filter on certian one or more regions, else
    # False to process all regions
    FilterRegions = False

    # ###--->>> Use a list to filter on regions.
    # Below are lists used to
    # test different regions
    #selected_regions = ['AI', 'EBS', 'GOA', 'GOM', 'NEUS_F', 'NEUS_S', 'SEUS_FALL', 'SEUS_SPR', 'SEUS_SUM', 'WC_ANN', 'WC_TRI',]

    selected_regions = ['AI',]

    # Test if we are filtering on regions. If so, a new table_names list is
    # created with the selected regions remaining in the list
    if FilterRegions:
        # New table_names list of lists #-> https://stackoverflow.com/questions/21507319/python-list-comprehension-list-of-lists
        table_names = [[r for r in group] for group in table_names if group[2] in selected_regions]
    else:
        selected_regions = ['AI', 'EBS', 'GOA', 'GOM', 'NEUS_F', 'NEUS_S', 'SEUS_FALL', 'SEUS_SPR', 'SEUS_SUM', 'WC_ANN', 'WC_TRI',]

    # https://pro.arcgis.com/en/pro-app/latest/arcpy/metadata/metadata-class.htm

    # Create Metadata XML function
    createEmptyTempMetadataXML()

    # Export Metadata Import Metadata
    #exportMetadata()

    #updateMetadata()

    #empty_metadata = os.path.join(BASE_DIRECTORY, 'DisMap Empty.xml')
    #prettyXML(empty_metadata)

    # https://pro.arcgis.com/en/pro-app/2.8/arcpy/metadata/metadata-class.htm

    # Save Inport and Template Metadata XML files
    # saveInportTemplateMetadata()

    # Import Template Metadata XML files
    # importTemplateMetadata()

    # Import Metadata to CRF datasets
    # importCrfMetadata()

    # Export a copy of the Metadata, using REMOVE_ALL_SENSITIVE_INFO
    # exportSelectedMetadata()

    # Export a copy of the Metadata, using a CUSTOM XLST file
    #exportInportMetadata()

    # Export a copy of the Metadata, using a CUSTOM XLST file
    #exportInportEntityMetadata()

    # Does nothing
    # main()

    arcpy.env.workspace = None
    arcpy.env.scratchWorkspace = None

##    print(">-> arcpy.management.Compact")
##    arcpy.management.Compact(ProjectGDB)
##    msg = arcpy.GetMessages()
##    msg = ">->-> {0}".format(msg.replace('\n', '\n>->-> '))
##    print(msg); del msg
