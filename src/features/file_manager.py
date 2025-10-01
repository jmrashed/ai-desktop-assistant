import os

class FileManager:
    def search_files(self, filename, directory="."):
        """Search for files"""
        try:
            matches = []
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if filename.lower() in file.lower():
                        matches.append(os.path.join(root, file))
            
            if matches:
                result = f"Found {len(matches)} files:\n"
                for match in matches[:5]:
                    result += f"- {match}\n"
                return result
            else:
                return f"No files found matching '{filename}'"
        except Exception as e:
            return f"Error searching files: {str(e)}"
    
    def create_folder(self, folder_name):
        """Create a new folder"""
        try:
            os.makedirs(folder_name, exist_ok=True)
            return f"Folder '{folder_name}' created successfully"
        except Exception as e:
            return f"Error creating folder: {str(e)}"