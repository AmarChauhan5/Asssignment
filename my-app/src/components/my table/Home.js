import React, { useState, useEffect, PureComponent } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
const axios = require("axios");

const Home = () => {
  const [data, setdata] = useState(null);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/")
      .then(function (response) {
        setdata(response.data);
      })
      .catch(function (error) {
        console.log(error);
      })
  }, []);
    console.log("Data :", data);
  return (
    <>
      <div className="d-flex flex-column h-100 px-5">
        <div className=" row flex-grow-1 h-75">
          <div className="col-6 h-100 d-flex justify-content-star align-items-center">
           <ResponsiveContainer width="100%" height="80%">
              <LineChart
                width={500}
                height={300}
                data={data}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5,
                  }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" interval={"preserveStartEnd"} />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line
                  type="monotone"
                  dataKey="my_close"
                  stroke="#8884d8"
                  activeDot={{ r: 8 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
          <div className="col-6 overflow-auto h-100 mb-5">
            <table className="table ">
              <thead className="head sticky-top">
                <tr>
                  <th className="px-2  text-center ">Date </th>
                  <th className="px-2  text-center">open </th>
                  <th className="px-2 text-center">high</th>
                  <th className="px-2 text-center">low</th>
                  <th className="px-2 text-center">close </th>
                  <th className="px-2 text-center">WPA</th>
                  <th className="px-2 text-nowrap text-center">
                    number of shares
                  </th>
                  <th className="px-2 text-nowrap text-center">
                    number of trades
                  </th>
                  <th className="px-2 text-nowrap text-center">
                    total turnover
                  </th>
                  <th className="px-2 text-nowrap text-center">
                    deliverable qauntity
                  </th>
                  <th className="px-2 text-nowrap text-center">
                    p_dei_qnty_to_trade_quanty
                  </th>
                  <th className="px-2 text-center">spread_h_l</th>
                  <th className="px-2 text-center">spread_c_o</th>
                </tr>
              </thead>
              <tbody>
                {data == null
                  ? ""
                  : data.map((data, index) => {
                      return (
                        <tr key={index} className="bg_two m-0 p-0">
                          <td className="text-center text-nowrap">
                            {" "}
                            {data.date}
                          </td>
                          <td className="text-center"> {data.my_open}</td>
                          <td className="text-center"> {data.high}</td>
                          <td className="text-center"> {data.low}</td>
                          <td className="text-center"> {data.my_close}</td>
                          <td className="text-center"> {data.wpa}</td>
                          <td className="text-center">{data.no_of_shares} </td>
                          <td className="text-center"> {data.no_of_trades}</td>
                          <td className="text-center">
                            {" "}
                            {data.total_turn_over}
                          </td>
                          <td className="text-center">
                            {data.deliverable_qauntity}
                          </td>
                          <td className="text-center">
                            {" "}
                            {data.p_dei_qnty_to_trade_quanty}
                          </td>
                          <td className="text-center"> {data.spread_h_l}</td>
                          <td className="text-center"> {data.spread_c_o}</td>
                        </tr>
                      );
                    })}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
