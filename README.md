# Nasa Space Apps 
 ExoSky project from the group Cation in Quito, Ecuador. We create a simulation of stars in the galaxy and exoplanet positions in space so that we can jump between exoplanets and see how the nightsky changes when you move across space. For this we rendered the actual positions of thousands of stars and for each planet recalculated each star's brighness concidering it's distance to each star

# Star Simulation Project

### Project Overview
This project is a star simulation environment built in Unity that showcases the stars of the night sky, including the Orion constellation, which is highlighted in red. The simulation supports switching perspectives to view the stars from various exoplanet locations. The project uses stellar data such as Right Ascension (RA), Declination (DEC), and Parallax to calculate the position of stars in the scene, while brightness is calculated dynamically based on the camera's distance from the stars.

### Unity Version
- **Unity Editor Version**: `2021.3.19f1`
  - To open the project, use Unity Editor version `2021.3.19f1` or higher for compatibility.

### Scene Components
- **Star Spawner Manager**: Responsible for spawning all stars in the simulation, using data from the star database.
- **Orion Constellation Manager**: Controls the display of the Orion constellation, which is rendered in red to differentiate it from other stars.

### Assets
- **Orion CSV File**: Contains data specific to the stars in the Orion constellation.
- **Stars Database CSV File**: Holds data for all 8,000 stars used in this simulation.
- **Exoplanets CSV File**: Contains information about exoplanets, which can be used as locations to spawn perspectives and view the sky in the app.

### Star Position and Brightness
- **Star Position**: The position of each star is determined using the `RA`, `DEC`, and `Parallax` values provided in the star database.
- **Star Brightness Calculation**:
  - The initial brightness is calculated based on Earth's position.
  - When switching to another exoplanet location, the brightness of each star is recalculated based on the camera's distance from the star.
  - The formula for recalculating brightness is:

    ```csharp
    star.calculatedBrightness = star.intrinsicBrightness + 5 * log10(distance / 10.0);
    ```

### Shader: Brightness Calculation
- The brightness recalculation for all stars is handled by a compute shader called **starBrightnessShader**, located in the **Scripts** folder.
- This shader dynamically updates the brightness of stars as the viewing perspective changes.

### How to Use
1. Open the project in Unity Editor version `2021.3.19f1` or newer.
2. Navigate to the main scene, which contains the star spawner and Orion constellation manager.
3. You can interact with the scene to view the stars, switch perspectives from Earth to other exoplanets, and watch the brightness of the stars adjust accordingly.
