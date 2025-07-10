import matplotlib.pyplot as plt
import seaborn as sns

# Set a modern Seaborn style and color palette globally
sns.set_theme(style="whitegrid", palette="Set2")


def plot_all(df):
    # Create a 2x2 subplot grid with larger figure size and proper spacing
    fig, axes = plt.subplots(2, 2, figsize=(20, 16))
    fig.suptitle('Google Play Store App Analysis', fontsize=24, fontweight='bold', y=0.98)
    
    # Distribution of App Ratings (top-left)
    sns.histplot(df['Rating'], bins=20, kde=True, color=sns.color_palette()[0], edgecolor='black', ax=axes[0,0])
    axes[0,0].set_title('Distribution of App Ratings', fontsize=16, fontweight='bold', pad=20)
    axes[0,0].set_xlabel('Rating', fontsize=14)
    axes[0,0].set_ylabel('Count', fontsize=14)
    axes[0,0].grid(axis='y', linestyle='--', alpha=0.7)

    # Top App Categories (top-right)
    top_categories = df['Category'].value_counts().head(10)
    sns.barplot(x=top_categories.values, y=top_categories.index, palette="viridis", ax=axes[0,1])
    axes[0,1].set_title('Top App Categories', fontsize=16, fontweight='bold', pad=20)
    axes[0,1].set_xlabel('Number of Apps', fontsize=14)
    axes[0,1].set_ylabel('Category', fontsize=14)
    axes[0,1].grid(axis='x', linestyle='--', alpha=0.7)

    # Rating vs Installs by App Type (bottom-left)
    scatter = sns.scatterplot(data=df, x='Rating', y='Installs', hue='Type', alpha=0.7, palette="Set1", s=50, edgecolor='w', linewidth=0.5, ax=axes[1,0])
    axes[1,0].set_title('Rating vs Installs by App Type', fontsize=16, fontweight='bold', pad=20)
    axes[1,0].set_xlabel('Rating', fontsize=14)
    axes[1,0].set_ylabel('Installs', fontsize=14)
    axes[1,0].legend(title='Type', fontsize=12, title_fontsize=13, loc='upper left')
    axes[1,0].grid(linestyle='--', alpha=0.6)

    # Boxplot of Ratings by App Type (bottom-right)
    sns.boxplot(data=df, x='Type', y='Rating', palette="pastel", ax=axes[1,1])
    axes[1,1].set_title('Boxplot of Ratings by App Type', fontsize=16, fontweight='bold', pad=20)
    axes[1,1].set_xlabel('Type', fontsize=14)
    axes[1,1].set_ylabel('Rating', fontsize=14)
    axes[1,1].grid(axis='y', linestyle='--', alpha=0.7)

    # Adjust layout with more spacing between subplots
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.08, right=0.95, hspace=0.3, wspace=0.3)
    plt.show()