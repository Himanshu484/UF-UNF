
# UF-UNF Collaboration Network Dashboard

An interactive web dashboard that visualizes research collaboration networks between the University of Florida (UF) and University of North Florida (UNF). This tool helps identify research partnerships, common publications, and collaboration patterns between researchers from both institutions.

🔗 **Live Dashboard**: [https://unf-uf-dashboard.onrender.com/](https://unf-uf-dashboard.onrender.com/)

## Features

- **Interactive Network Visualization**: Explore researcher networks with connected nodes representing collaboration relationships
- **Lasso Selection**: Select multiple researchers to discover their joint publications
- **Hover Information**: View researcher details including name, research area, and affiliation
- **Color-coded Affiliations**: Easy identification of UF vs UNF researchers
- **Publication Details**: Access titles and abstracts of collaborative research papers

## Technology Stack

- **Python**: Core programming language
- **Dash**: Web application framework
- **Plotly**: Interactive visualization library
- **Pandas**: Data manipulation and analysis
- **HTML/CSS**: Frontend styling

## Usage

### Exploring the Network
- Each point represents a researcher from either UF or UNF
- Lines between points indicate collaboration relationships
- Point sizes reflect the researcher's collaboration intensity

### Finding Joint Publications
1. Use the lasso selection tool (click and drag to select multiple researchers)
2. Selected researchers will be highlighted
3. The dashboard will automatically display:
   - Names of selected researchers
   - List of their joint publications with titles and abstracts

## Data Sources

The dashboard uses three main datasets:
- `nodes_final.csv`: Researcher information and network positions
- `node_list.csv`: Publication and researcher mapping data
- `edge_list.csv`: Collaboration relationships between researchers

## Project Structure

```
UF-UNF/
├── app.py                 # Main Dash application
├── assets/
│   ├── nodes_final.csv    # Researcher network data
│   ├── node_list.csv      # Publication-researcher mapping
│   └── edge_list.csv      # Collaboration edges
└── README.md
```

## Deployment

The application is deployed on Render and accessible at: https://unf-uf-dashboard.onrender.com/

## Research Applications

This dashboard supports:
- **Academic Collaboration Analysis**: Identify research partnerships and potential collaboration opportunities
- **Interdisciplinary Research**: Discover cross-institutional research themes
- **Publication Impact**: Analyze joint research outputs between institutions
- **Network Analysis**: Understand the structure of academic collaboration networks

---

*This project visualizes research collaboration data to promote academic partnerships between the University of Florida and University of North Florida.*
