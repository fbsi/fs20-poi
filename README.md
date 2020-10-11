# fs20-poi :plane:
Creating a MSFS2020 Flight Simulator SDK readable .xml File from .cup with POI to display in the simulator.
## How-To build in the SDK
- Folder stucture
- New project
- New module + fill out some description (BGL, Scenery)
- Asset diretory should be scene folder in project directory
- Create object Landmark POI
- Save scenery in project folder
- Close project in sim
- Replace contents of scenery file .xml with output in file.xml
the contents of the file should look like this
```xml
<?xml version="1.0"?>
<FSData version="9.0">
	<LandmarkLocation instanceId="{CD544AFF-EF0D-4398-BA1F-5510298690E2}" type="POI" name="Zugspitzetest" lat="47.42111976520967" lon="10.98492037240454" alt="2913.99726566113532"/>
</FSData>
```
- Open project again
- Build All (Errors dont matter as long you are in the plane when building)
- Close project and sim
- Check Packages folder for new generated file in the scenery-sub-subfolder
- Copy the project folder generated in Packages to your Community Folder
> the community folder most likely on steam installations can be found under D:\SteamLibrary\steamapps\common\MicrosoftFlightSimulator\Packages\Community

## Known problems
The altitude parameter doesnt seem to match with real values in the sim, so factor 0.1 is applied.
