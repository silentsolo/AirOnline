var lineChart = echarts.init(document.getElementById('line'));
option = {
    backgroundColor : 'rgb(255,255,255)',
    tooltip : {
        trigger: 'axis'
    },
    calculable : true,
    xAxis : [
        {
            name : "月(时间)",
            type : 'category',
            boundaryGap : false,
            data : ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
        }
    ],
    yAxis : [
        {
            name : "TOP1 CITY AQI(空气质量)",
            splitNumber : 3,
            type : 'value',
            axisLabel : {
                formatter: '{value}'
            }
        }
    ],
    series : [
        {
            name:'AQI',
            type:'line',
            data:[],

            itemStyle : {
                normal: {
                    color : 'rgb(8,93,56)'
                },
                emphasis: {
                    color : 'rgb(8,93,56)'
                }
            },
            markLine : {
                data : [
                    {type : 'average', name: '平均值'}
                ]
            }
        }
    ]
};
lineChart.setOption(option);