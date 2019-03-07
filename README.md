# Operationalizing a Deep Learning model (CNN) using ONNX, Keras, Tensorflow, and Flask

# What is ONNX?

ONNX (Open Neural Network Exchange) is an open format that represents deep learning models. It is a community project championed by Facebook and Microsoft. Currently there are many libraries and frameworks which do not interoperate, hence, the developers are often locked into using one framework or ecosystem. The goal of ONNX is to enable these libraries and frameworks to work together by sharing of models.

# Why ONNX?

ONNX provides an intermediate representation (IR) of models (see below), whether a model is created using CNTK, TensorFlow or another framework. The IR representation allows deployment of ONNX models to various targets, such as IoT, Windows, Azure or iOS/Android.

<img src="images/onnxgraph.png" alt="onnxgraph" style="display: block; margin-left: auto; margin-right: auto; width: 50%;" width="600" height="600"/>

The intermediate representation provides data scientist with the ability to choose the best framework and tool for the job at hand, without having to worry about how it will be deployed and optimized for the deployment target.

# How ONNX?

ONNX provides two core components:
- Extensible computational graph model. This model is represented as an acyclic graph, consisting of a list of nodes with edges. It also contains metadata information,
such as author, version, etc.
- Operators. These form the nodes in a graph. They are portable across the frameworks and are currently of three types.
 - Core Operators - These are supported by all ONNX-compatible products.
 - Experimental Operators - Either supported or deprecated within few months.
 - Custom Ops - which are specific to a framework or runtime.

> PySyft supports Python &gt;= 3.6 and PyTorch 1.0.0

```bash
pip install syft
```
## Run Local Notebook Server
All the examples can be played with by running the command
```bash
make notebook
```
and selecting the pysyft kernel

## Try out the Tutorials

A comprehensive list of tutorials can be found [here](https://github.com/OpenMined/PySyft/tree/master/examples/tutorials)

These tutorials cover how to perform techniques such as federated learning and differential privacy using PySyft.

## Start Contributing

The guide for contributors can be found [here](https://github.com/OpenMined/PySyft/tree/master/CONTRIBUTING.md). It covers all that you need to know to start contributing code to PySyft in an easy way.

Also join the rapidly growing community of 2500+ on [Slack](http://slack.openmined.org). The slack community is very friendly and great about quickly answering questions about the use and development of PySyft!

## Troubleshooting

We have written an installation example in [this colab notebook](https://colab.research.google.com/drive/14tNU98OKPsP55Y3IgFtXPfd4frqbkrxK), you can use it as is to start working with PySyft on the colab cloud, or use this setup to fix your installation locally.

## Organizational Contributions

We are very grateful for contributions to PySyft from the following organizations!

 <img src="https://raw.githubusercontent.com/coMindOrg/federated-averaging-tutorials/master/images/comindorg_logo.png" alt="coMind" width="200" height="130"/>  

 [coMind Website](https://comind.org/) & [coMind Github](https://github.com/coMindOrg/federated-averaging-tutorials)

## Disclaimer

Do NOT use this code to protect data (private or otherwise) - at present it is very insecure.

## License

[Apache License 2.0](https://github.com/OpenMined/PySyft/blob/master/LICENSE)

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fmatthew-mcateer%2FPySyft.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fmatthew-mcateer%2FPySyft?ref=badge_large)
