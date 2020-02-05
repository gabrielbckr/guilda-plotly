import React from 'react';
import Plot from 'react-plotly.js';
import plot_2d from '../src/plot_2d.json'
import plot_3d from '../src/plot_3d.json'

class App extends React.Component {
  render() {
    return (
      <div>
      <Plot
        data={plot_2d.data}
        layout={plot_2d.layout}
      />
      <Plot
        data={plot_3d.data}
        layout={plot_3d.layout}
      />
      <h1>adf</h1>
      </div>
    );
  }
}
export default App;