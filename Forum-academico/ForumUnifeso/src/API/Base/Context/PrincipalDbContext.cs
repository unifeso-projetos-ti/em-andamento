using ForumUnifeso.src.API.Model;
using Microsoft.EntityFrameworkCore;

namespace ForumUnifeso.src.API.Base.Context
{
    public class PrincipalDbContext : DbContext
    {
        public PrincipalDbContext(DbContextOptions<PrincipalDbContext> options) : base(options)
        {
        }

        public DbSet<Post> Post { get; set; } = null!;
        public DbSet<Person> Person { get; set; } = null!;
        public DbSet<ThreadForum> ThreadForum { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            // Mapeamento da classe Post
            modelBuilder.Entity<Post>(entity =>
            {
                entity.HasKey(e => e.Id);

                entity.Property(e => e.Id)
                 .ValueGeneratedOnAdd(); 

                entity.Property(e => e.Title)
                      .IsRequired()
                      .HasMaxLength(200); 

                entity.Property(e => e.Description)
                      .HasMaxLength(1000); 

                entity.Property(e => e.Date)
                      .IsRequired(); 

                // Relacionamento com Person (Autor)
                entity.HasOne(e => e.Author)
                  .WithMany(p => p.Posts) 
                  .HasForeignKey(e => e.AuthorId) 
                  .IsRequired();

                // Relacionamento com ThreadForum (ThreadForum)
                entity.HasOne(e => e.ThreadForum)
                  .WithMany(tf => tf.Answers)
                  .HasForeignKey(e => e.ThreadForumId)
                  .OnDelete(DeleteBehavior.SetNull);
            });

            // Mapeamento da classe ThreadForum
            modelBuilder.Entity<ThreadForum>(entity =>
            {
                entity.HasKey(e => e.Id); 

                entity.Property(e => e.Id)
                .ValueGeneratedOnAdd();

                // Relacionamento com Post (Topic)
                entity.HasOne(e => e.Topic)
                  .WithOne() 
                  .HasForeignKey<ThreadForum>(e => e.TopicId) 
                  .OnDelete(DeleteBehavior.Restrict);

                // Relacionamento com Posts (Answers)
                entity.HasMany(e => e.Answers)
                  .WithOne(p => p.ThreadForum)
                  .HasForeignKey(p => p.ThreadForumId)
                  .OnDelete(DeleteBehavior.SetNull);
            });

            // Mapeamento da classe Person
            modelBuilder.Entity<Person>(entity =>
            {
                entity.HasKey(e => e.Id); 

                entity.Property(e => e.Id)
                .ValueGeneratedOnAdd();

                entity.Property(e => e.Name)
                      .IsRequired()
                      .HasMaxLength(100); 

                // Relacionamento com Post (Autor)
                entity.HasMany(e => e.Posts)
                      .WithOne(p => p.Author)
                      .HasForeignKey(p => p.AuthorId); 
            });
        }
    }
}
