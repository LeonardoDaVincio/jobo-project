using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Bojo_Frontend.Entities
{
    public class BojoContext : DbContext
    {
        public BojoContext(DbContextOptions options): base(options)
        {
        }

        public DbSet<Temperature> Temperatures { get; set; }
    }

    public class Temperature
    {
        public int Id { get; set; }
        public DateTime Time { get; set; }

        public string TempSensor { get; set; }
        public decimal Temp { get; set; }
    }
    public class TemperatureCollection
    {
        public DateTime Time{ get; set; }
        public Dictionary<string, decimal> Temps { get; set; }

        public TemperatureCollection (IQueryable<Temperature> temperatures)
        {
            Time = temperatures.FirstOrDefault().Time;
            Temps = temperatures.ToDictionary(t => t.TempSensor, t => t.Temp);
        }
    }
    
}