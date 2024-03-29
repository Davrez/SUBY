o
    tZ�b~  �                   @   s�   d dl Z d dlZd dlZd dlZG dd� d�Zg d�ZdZdZdZdZ	d	Z
d
d� Zdd� Zdd� Zdd� ZedkrJe� jZe�  ee� ee� dS dS )�    Nc                   @   s   e Zd ZdZdZdZdS )�bcolors�[93m�[91m�[0mN)�__name__�
__module__�__qualname__�WARNING�FAIL�ENDC� r   r   �suby.pyr      s    r   )zhttp://zhttps://Zwwwz[92mr   r   r   z
[1;37;40mc                  C   s   t �� } | �d� | �� S )N�domain)�argparse�ArgumentParser�add_argument�
parse_args)�parserr   r   r   �args   s   
r   c                   C   s.   t d�tttt�� t tj� dtj� �� d S )Na�  {}
 ::::::::  :::    ::: :::::::::  :::   ::: 
:+:    :+: :+:    :+: :+:    :+: :+:   :+: 
+:+        +:+    +:+ +:+    +:+  +:+ +:+  
+#++:++#++ +#+    +:+ +#++:++#+    +#++:   
       +#+ +#+    +#+ +#+    +#+    +#+    
#+#    #+# #+#    #+# #+#    #+#    #+#    
 ########   ########  #########     ###    

    {}
               {} 
 _____ _____ _____ _____ _____ _____
|_____|NEW__|_____|_____|_____|_____|
|_____|_____|FREE_|NET__|SCAN_|TOOL_| {}
    z:NOTE: Use this tool with internet subscriptions or bundles)�print�format�Y�Wr   r	   r   r   r   r   r   �banner   s   �r   c                 C   s*   t D ]}|| v rtd� t��  q	 qd S )Nz Usage: python suby.py domain.com)�_stripr   �sys�exit)r   �tr   r   r   �clean%   s   
�r   c           	      C   s�   d}d| i}dddddd�}z/t j|||d	d
�j}t�|�}|d }td�|d �� |D ]\}}td�t|t�� q-W d S  tyy   td� tt	j
� dt	j� �� td� td�| �� td� td� td� td� td� td� Y d S w )Nz,https://domains.yougetsignal.com/domains.phpZremoteAddresszdomains.yougetsignal.comz
keep-alivezno-cachezhttp://www.yougetsignal.comz�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36)ZHostZ
ConnectionzCache-ControlZOriginz
User-Agent�   )Zheaders�dataZtimeoutZdomainArrayzA[33m
Total of domains found: {}
---------------------------[0m
ZdomainCountz{}{}{}� u
   ERROR ⚠ z+===========================================zThere is a problem with {}z
USAGE:
z[suby.py example.com]z

z
>> Use a valid domain\IP
z#
>> check your internet Connection
)�requestsZpost�content�json�loadsr   r   r   �BaseExceptionr   r
   r   )	ZdomZ_api�_dataZ_headersZresponseZ_jsonr#   �d�ur   r   r   �rev-   sN   ���
����r*   �__main__)r"   r$   r   r   r   r   �Gr   �Rr   �Ir   r   r   r*   r   r   r   r   r   r   �<module>   s*    *�