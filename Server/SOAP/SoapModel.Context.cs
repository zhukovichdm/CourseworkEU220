﻿//------------------------------------------------------------------------------
// <auto-generated>
//     Этот код создан по шаблону.
//
//     Изменения, вносимые в этот файл вручную, могут привести к непредвиденной работе приложения.
//     Изменения, вносимые в этот файл вручную, будут перезаписаны при повторном создании кода.
// </auto-generated>
//------------------------------------------------------------------------------

namespace SOAP
{
    using System;
    using System.Data.Entity;
    using System.Data.Entity.Infrastructure;
    
    public partial class CourseworkDBContext : DbContext
    {
        public CourseworkDBContext()
            : base("name=CourseworkDBContext")
        {
        }
    
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            throw new UnintentionalCodeFirstException();
        }
    
        public virtual DbSet<Contents> Contents { get; set; }
        public virtual DbSet<ContentTypes> ContentTypes { get; set; }
        public virtual DbSet<Subscriptions> Subscriptions { get; set; }
        public virtual DbSet<Topics> Topics { get; set; }
        public virtual DbSet<Users> Users { get; set; }
    }
}
