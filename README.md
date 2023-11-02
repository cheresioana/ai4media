# MindBugs Discovery project adapted for AI4Experiments platform

## General description

![Pipeline](docs/pipeline.png) 

The pipeline begins with a DataBroker, responsible for collecting structured data containing "statement" and "label" information. This dataset then moves to the Aggregator component, which plays a role in processing the data.

The Aggregator serves a dual purpose. It not only trains a classifier but also extracts relevant keywords from a variety of statements, making the data more informative.

The next player in this sequence is the Knowledge Graph (KG) component. Leveraging the Aggregator's expertise, the KG component analyzes and classifies statements. It also searches its disinformation graph to find the closest match to the analyzed statement.

Using the Louvain algorithm, the KG component identifies and highlights the disinformation community associated with the analyzed statement. This step provides valuable insights into the relationships and associations within the disinformation landscape.


